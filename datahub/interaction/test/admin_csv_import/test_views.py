import gzip
import io

import pytest
from django.conf import settings
from django.contrib import messages as django_messages
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.core.cache import cache
from django.test import Client
from django.urls import reverse
from rest_framework import status

from datahub.company.contact_matching import ContactMatchingStatus
from datahub.company.test.factories import AdviserFactory
from datahub.core.exceptions import DataHubException
from datahub.core.test_utils import AdminTestMixin, create_test_user
from datahub.feature_flag.test.factories import FeatureFlagFactory
from datahub.interaction.admin_csv_import.cache_utils import _cache_key_for_token, CacheKeyType
from datahub.interaction.admin_csv_import.views import (
    INTERACTION_IMPORTER_FEATURE_FLAG_NAME,
    INVALID_TOKEN_MESSAGE,
)
from datahub.interaction.models import Interaction, InteractionPermission
from datahub.interaction.test.admin_csv_import.utils import (
    make_csv_file,
    make_csv_file_from_dicts,
    make_matched_rows,
    make_multiple_matches_rows,
    make_unmatched_rows,
    random_communication_channel,
    random_service,
)


@pytest.fixture()
def interaction_importer_feature_flag():
    """Creates the import interactions tool feature flag."""
    yield FeatureFlagFactory(code=INTERACTION_IMPORTER_FEATURE_FLAG_NAME)


import_interactions_url = reverse(
    admin_urlname(Interaction._meta, 'import'),
)
interaction_change_list_url = reverse(
    admin_urlname(Interaction._meta, 'changelist'),
)
import_save_urlname = admin_urlname(Interaction._meta, 'import-save')
import_complete_urlname = admin_urlname(Interaction._meta, 'import-complete')


class TestInteractionAdminChangeList(AdminTestMixin):
    """Tests for the contact admin change list."""

    @pytest.mark.usefixtures('interaction_importer_feature_flag')
    def test_load_import_link_exists(self):
        """
        Test that there is a link to import interactions on the interaction change list page.
        """
        response = self.client.get(interaction_change_list_url)
        assert response.status_code == status.HTTP_200_OK

        assert import_interactions_url in response.rendered_content

    def test_import_link_does_not_exist_if_only_has_view_permission(self):
        """
        Test that there is not a link to import interactions if the user only has the delete
        (but not change) permission for interactions.
        """
        user = create_test_user(
            permission_codenames=(InteractionPermission.view_all,),
            is_staff=True,
            password=self.PASSWORD,
        )

        client = self.create_client(user=user)
        response = client.get(interaction_change_list_url)
        assert response.status_code == status.HTTP_200_OK

        assert f'Select {Interaction._meta.verbose_name} to view' in response.rendered_content
        assert import_interactions_url not in response.rendered_content

    def test_import_link_does_not_exist_if_feature_flag_inactive(self):
        """
        Test that there is not a link to import interactions if the feature flag is inactive.
        """
        response = self.client.get(interaction_change_list_url)
        assert response.status_code == status.HTTP_200_OK

        assert import_interactions_url not in response.rendered_content


@pytest.mark.usefixtures('interaction_importer_feature_flag')
@pytest.mark.parametrize(
    'http_method,url',
    (
        ('get', import_interactions_url),
        ('post', import_interactions_url),
        ('post', reverse(import_save_urlname, kwargs={'token': 'test-token'})),
        ('get', reverse(import_complete_urlname, kwargs={'token': 'test-token'})),
    ),
)
class TestAccessRestrictions(AdminTestMixin):
    """Tests permissions and other access restrictions on import interaction-related views."""

    def test_redirects_to_login_page_if_not_logged_in(self, http_method, url):
        """Test that the view redirects to the login page if the user isn't authenticated."""
        client = Client()
        # Note: Client.generic() doesn't support follow=True
        request_func = getattr(client, http_method)
        response = request_func(url, follow=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.redirect_chain == [
            (self.login_url_with_redirect(url), status.HTTP_302_FOUND),
        ]

    def test_redirects_to_login_page_if_not_staff(self, url, http_method):
        """Test that the view redirects to the login page if the user isn't a member of staff."""
        user = create_test_user(is_staff=False, password=self.PASSWORD)

        client = self.create_client(user=user)
        # Note: Client.generic() doesn't support follow=True
        request_func = getattr(client, http_method)
        response = request_func(url, follow=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.redirect_chain == [
            (self.login_url_with_redirect(url), status.HTTP_302_FOUND),
        ]

    def test_permission_denied_if_staff_and_without_change_permission(self, url, http_method):
        """
        Test that the view returns a 403 response if the staff user does not have the
        change interaction permission.
        """
        user = create_test_user(
            permission_codenames=(InteractionPermission.view_all,),
            is_staff=True,
            password=self.PASSWORD,
        )

        client = self.create_client(user=user)
        response = client.generic(http_method, url)
        assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize(
    'http_method,url',
    (
        ('get', import_interactions_url),
        ('post', import_interactions_url),
        ('post', reverse(import_save_urlname, kwargs={'token': 'test-token'})),
        ('get', reverse(import_complete_urlname, kwargs={'token': 'test-token'})),
    ),
)
class Test404IfFeatureFlagDisabled(AdminTestMixin):
    """
    Tests that import interaction-related views return a 404 if the feature flag is not
    active.

    (The feature flag not being active is implicit by it not being created,)
    """

    def test_returns_404_if_feature_flag_inactive(self, http_method, url):
        """Test that the a 404 is returned if the feature flag is inactive."""
        response = self.client.generic(
            http_method,
            url,
            data={},
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.usefixtures('interaction_importer_feature_flag', 'local_memory_cache')
class TestImportInteractionsSelectFileView(AdminTestMixin):
    """Tests for the import interaction select file form."""

    def test_displays_page_if_with_correct_permissions(self):
        """
        Test that the view returns displays the form if the feature flag is active
        and the user has the correct permissions.
        """
        response = self.client.get(import_interactions_url)

        assert response.status_code == status.HTTP_200_OK
        assert 'form' in response.context

    def test_does_not_allow_file_without_correct_columns(self):
        """Test that the form rejects a CSV file that doesn't have the required columns."""
        file = make_csv_file(
            ('test',),
            ('row',),
        )

        response = self.client.post(
            import_interactions_url,
            data={
                'csv_file': file,
            },
        )

        assert response.status_code == status.HTTP_200_OK

        form = response.context['form']

        assert 'csv_file' in form.errors
        assert form.errors['csv_file'] == [
            'This file is missing the following required columns: '
            'adviser_1, contact_email, date, kind, service.',
        ]

    def test_rejects_large_files(self):
        """
        Test that large files are rejected.

        Note: INTERACTION_ADMIN_CSV_IMPORT_MAX_SIZE is set to 5 kB in config.settings.test
        """
        file_size = settings.INTERACTION_ADMIN_CSV_IMPORT_MAX_SIZE + 1
        file = io.BytesIO(b'-' * file_size)
        file.name = 'test.csv'

        response = self.client.post(
            import_interactions_url,
            data={
                'csv_file': file,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        messages = list(response.context['messages'])
        assert len(messages) == 1
        assert messages[0].level == django_messages.ERROR
        assert messages[0].message == (
            'The file test.csv was too large. Files must be less than 5.0 KB.'
        )

    @pytest.mark.parametrize(
        'max_errors,should_be_truncated',
        (
            (5, True),
            (10, False),
        ),
    )
    def test_displays_errors_for_file_with_invalid_rows(
        self,
        max_errors,
        should_be_truncated,
        monkeypatch,
    ):
        """Test that errors are displayed for a file with invalid rows."""
        monkeypatch.setattr(
            'datahub.interaction.admin_csv_import.views.MAX_ERRORS_TO_DISPLAY',
            max_errors,
        )

        # This file should have 10 errors
        file = make_csv_file(
            ('kind', 'date', 'adviser_1', 'contact_email', 'service'),
            ('invalid', 'invalid', 'invalid', 'invalid', 'invalid'),
            ('invalid', 'invalid', 'invalid', 'invalid', 'invalid'),
        )

        response = self.client.post(
            import_interactions_url,
            data={
                'csv_file': file,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert len(response.context['errors']) == min(10, max_errors)
        assert response.context['are_errors_truncated'] == should_be_truncated

    def test_displays_no_matches_message_if_no_matches(self):
        """
        Test that if a valid file is uploaded but no records are matched to contacts,
        the import_no_matches.html template is used.
        """
        adviser = AdviserFactory()
        service = random_service()
        communication_channel = random_communication_channel()
        file = make_csv_file(
            (
                'kind',
                'date',
                'adviser_1',
                'contact_email',
                'service',
                'communication_channel',
            ),
            (
                'interaction',
                '01/01/2018',
                adviser.name,
                'person@company.uk',
                service.name,
                communication_channel.name,
            ),
        )

        response = self.client.post(
            import_interactions_url,
            data={
                'csv_file': file,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.template_name.endswith('/import_no_matches.html')
        assert response.context['num_matched'] == 0
        assert response.context['num_unmatched'] == 1
        assert response.context['num_multiple_matches'] == 0
        assert response.context['matched_rows'] == []
        assert response.context['num_matched_omitted'] == 0

    @pytest.mark.parametrize(
        'num_input_rows,expected_num_omitted_rows',
        (
            (2, 0),
            (10, 5),
        ),
    )
    def test_shows_preview_if_matches(
        self,
        num_input_rows,
        expected_num_omitted_rows,
        monkeypatch,
        # _,
    ):
        """
        Test that if a valid file is uploaded and some records are matched to contacts,
        the import_preview.html template is used with an appropriate context.
        """
        max_preview_rows = 5
        monkeypatch.setattr(
            'datahub.interaction.admin_csv_import.views.MAX_PREVIEW_ROWS_TO_DISPLAY',
            max_preview_rows,
        )

        csv_rows = make_matched_rows(num_input_rows)
        file = make_csv_file_from_dicts(*csv_rows)

        response = self.client.post(
            import_interactions_url,
            data={
                'csv_file': file,
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.template_name.endswith('/import_preview.html')
        assert response.context['num_matched'] == num_input_rows
        assert response.context['num_unmatched'] == 0
        assert response.context['num_multiple_matches'] == 0
        assert len(response.context['matched_rows']) == min(max_preview_rows, num_input_rows)
        assert response.context['num_matched_omitted'] == expected_num_omitted_rows


@pytest.mark.usefixtures('interaction_importer_feature_flag', 'local_memory_cache')
class TestImportInteractionsSaveView(AdminTestMixin):
    """Tests for the import interaction save view."""

    def test_redirects_and_displays_error_if_token_invalid(self):
        """
        Test that the user is redirected to the change list and an error is displayed if the
        token is invalid.
        """
        url = reverse(
            import_save_urlname,
            kwargs={'token': 'invalid-token'},
        )
        response = self.client.post(url, follow=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.redirect_chain == [
            (interaction_change_list_url, status.HTTP_302_FOUND),
        ]

        messages = list(response.context['messages'])
        assert len(messages) == 1
        assert messages[0].level == django_messages.ERROR
        assert messages[0].message == INVALID_TOKEN_MESSAGE

    def test_raises_error_if_file_in_cache_is_invalid(self):
        """
        Test that if the file in the cache fails InteractionCSVForm re-validation,
        a DataHubException is raised.

        (This should not happen in normal circumstances.)
        """
        token = 'test-token'
        compressed_conents = gzip.compress(b'invalid')
        contents_key = _cache_key_for_token(token, CacheKeyType.file_contents)
        name_key = _cache_key_for_token(token, CacheKeyType.file_name)

        cache.set(contents_key, compressed_conents)
        cache.set(name_key, 'test.csv')

        url = reverse(
            import_save_urlname,
            kwargs={'token': token},
        )
        with pytest.raises(DataHubException):
            self.client.post(url)

    @pytest.mark.parametrize('num_matching', (5, 10))
    @pytest.mark.parametrize('num_unmatched', (0, 6))
    @pytest.mark.parametrize('num_multiple_matches', (0, 6))
    def test_creates_interactions(self, num_matching, num_unmatched, num_multiple_matches):
        """
        Test that interactions are created if a valid token is provided, and that the
        user is redirected to the import complete page.

        Note: The full saving logic is tested in the InteractionCSVForm tests.
        """
        token = 'test-token'
        matching_rows = _create_file_in_cache(
            token,
            num_matching,
            num_unmatched,
            num_multiple_matches,
        )

        url = reverse(
            import_save_urlname,
            kwargs={'token': token},
        )
        response = self.client.post(url)
        assert response.status_code == status.HTTP_302_FOUND
        expected_redirect_url = reverse(
            import_complete_urlname,
            kwargs={'token': token},
        )
        assert response.url == expected_redirect_url

        created_interactions = list(Interaction.objects.all())
        assert len(created_interactions) == num_matching

        expected_contact_emails = {row['contact_email'] for row in matching_rows}
        actual_contact_emails = {
            interaction.contacts.first().email for interaction in created_interactions
        }
        # Make sure the test was correctly set up with unique contact emails
        assert len(actual_contact_emails) == num_matching
        # Check that the interactions created are the ones we expect
        # Note: the full saving logic for a row is tested in the InteractionCSVRowForm tests
        assert expected_contact_emails == actual_contact_emails

        # Check that created_by is set correctly
        assert all([
            interaction.created_by == self.user for interaction in created_interactions
        ])

    @pytest.mark.parametrize('num_matching', (5, 10))
    @pytest.mark.parametrize('num_unmatched', (0, 6))
    @pytest.mark.parametrize('num_multiple_matches', (0, 6))
    def test_saves_results(self, num_matching, num_unmatched, num_multiple_matches):
        """Test that counts by matching status are saved in the cache."""
        token = 'test-token'
        _create_file_in_cache(token, num_matching, num_unmatched, num_multiple_matches)

        url = reverse(
            import_save_urlname,
            kwargs={'token': token},
        )
        response = self.client.post(url)
        assert response.status_code == status.HTTP_302_FOUND

        expected_redirect_url = reverse(
            import_complete_urlname,
            kwargs={'token': token},
        )
        assert response.url == expected_redirect_url

        cache_key = _cache_key_for_token(token, CacheKeyType.result_counts_by_status)
        matching_counts = cache.get(cache_key)
        assert matching_counts == {
            ContactMatchingStatus.matched: num_matching,
            ContactMatchingStatus.unmatched: num_unmatched,
            ContactMatchingStatus.multiple_matches: num_multiple_matches,
        }


@pytest.mark.usefixtures('interaction_importer_feature_flag', 'local_memory_cache')
class TestImportInteractionsCompleteView(AdminTestMixin):
    """Tests for the import complete view."""

    def test_redirects_and_displays_error_if_token_invalid(self):
        """
        Test that the user is redirected to the change list and an error is displayed if the
        token is invalid.
        """
        url = reverse(
            import_complete_urlname,
            kwargs={'token': 'invalid-token'},
        )
        response = self.client.post(url, follow=True)

        assert response.status_code == status.HTTP_200_OK
        assert response.redirect_chain == [
            (interaction_change_list_url, status.HTTP_302_FOUND),
        ]

        messages = list(response.context['messages'])
        assert len(messages) == 1
        assert messages[0].level == django_messages.ERROR
        assert messages[0].message == INVALID_TOKEN_MESSAGE

    @pytest.mark.parametrize('num_matching', (1, 2))
    @pytest.mark.parametrize('num_unmatched', (0, 1, 3))
    @pytest.mark.parametrize('num_multiple_matches', (0, 1, 4))
    def test_displays_counts_by_status(self, num_matching, num_unmatched, num_multiple_matches):
        """Test that counts are displayed for each matching status."""
        token = 'test-token'
        cache_key = _cache_key_for_token(token, CacheKeyType.result_counts_by_status)
        cache_value = {
            ContactMatchingStatus.matched: num_matching,
            ContactMatchingStatus.unmatched: num_unmatched,
            ContactMatchingStatus.multiple_matches: num_multiple_matches,
        }
        cache.set(cache_key, cache_value)

        url = reverse(
            import_complete_urlname,
            kwargs={'token': token},
        )
        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.context['num_matched'] == num_matching
        assert response.context['num_unmatched'] == num_unmatched
        assert response.context['num_multiple_matches'] == num_multiple_matches


def _create_file_in_cache(token, num_matching, num_unmatched, num_multiple_matches):
    matched_rows = make_matched_rows(num_matching)
    unmatched_rows = make_unmatched_rows(num_unmatched)
    multiple_matches_rows = make_multiple_matches_rows(num_multiple_matches)

    file = make_csv_file_from_dicts(
        *matched_rows,
        *unmatched_rows,
        *multiple_matches_rows,
        filename='cache-test.csv',
    )
    with file:
        compressed_contents = gzip.compress(file.read())
    contents_key = _cache_key_for_token(token, CacheKeyType.file_contents)
    name_key = _cache_key_for_token(token, CacheKeyType.file_name)

    cache.set(contents_key, compressed_contents)
    cache.set(name_key, file.name)

    return matched_rows
