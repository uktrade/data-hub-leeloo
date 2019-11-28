from datetime import datetime, time, timedelta

from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils.timezone import now
from django_pglocks import advisory_lock
from rest_framework.status import is_server_error

from datahub.company.models import Company
from datahub.dnb_api.utils import (
    DNBServiceConnectionError,
    DNBServiceError,
    DNBServiceTimeoutError,
    get_company,
    get_company_update_page,
    update_company_from_dnb,
)

logger = get_task_logger(__name__)


def _sync_company_with_dnb(company_id, fields_to_update, task):
    dh_company = Company.objects.get(id=company_id)

    try:
        dnb_company = get_company(dh_company.duns_number)
    except DNBServiceError as exc:
        if is_server_error(exc.status_code):
            raise task.retry(exc=exc, countdown=60)
        raise
    except (DNBServiceConnectionError, DNBServiceTimeoutError) as exc:
        raise task.retry(exc=exc, countdown=60)

    update_company_from_dnb(
        dh_company,
        dnb_company,
        fields_to_update=fields_to_update,
        update_descriptor='celery:sync_company_with_dnb',
    )


@shared_task(
    bind=True,
    acks_late=True,
    priority=9,
    max_retries=3,
)
def sync_company_with_dnb(self, company_id, fields_to_update=None):
    """
    Sync a company record with data sourced from DNB. `company_id` identifies the
    company record to sync and `fields_to_update` defines an iterable of
    company serializer fields that should be updated - if it is None, all fields
    will be synced.
    """
    _sync_company_with_dnb(company_id, fields_to_update, self)


def _get_company_updates(task, last_updated_after, fields_to_update):
    yesterday = now() - timedelta(days=1)
    midnight_yesterday = datetime.combine(yesterday, time.min)
    last_updated_after = last_updated_after or midnight_yesterday.isoformat()
    cursor = None

    # TODO: In a following PR, we will bind this loop to an upper-limit
    # on the number of records that we would like to update in a run.
    while True:

        try:
            response = get_company_update_page(last_updated_after, cursor)

        except DNBServiceError as exc:
            if is_server_error(exc.status_code):
                raise task.retry(exc=exc, countdown=60)
            raise

        except (DNBServiceConnectionError, DNBServiceTimeoutError) as exc:
            raise task.retry(exc=exc, countdown=60)

        # Spawn tasks that updates Data Hub companies
        for data in response.get('results', []):
            update_company.apply_async(
                data,
                fields_to_update=fields_to_update,
            )

        cursor = response.get('next')
        if cursor is None:
            break


@shared_task(
    bind=True,
    acks_late=True,
    priority=9,
    max_retries=3,
    queue='long-running',
)
def get_company_updates(self, last_updated_after=None, fields_to_update=None):
    """
    Gets the lastest updates for D&B companies from dnb-service.

    The `dnb-service` exposes these updates as a cursor-paginated list. This
    task goes through the pages and spawns tasks that update the records in
    Data Hub.
    """
    with advisory_lock('get_company_updates', wait=False) as acquired:

        if not acquired:
            logger.info('Another instance of this task is already running.')
            return

        _get_company_updates(self, last_updated_after, fields_to_update)


@shared_task(
    bind=True,
    acks_late=True,
    priority=9,
    max_retries=3,
)
def update_company(self, data, fields_to_update=None):
    """
    Get the latest updates for D&B companies from dnb-service. This is a stub at
    the moment and will become a thin wrapper around `utils.update_company_from_dnb`.
    """
    raise NotImplementedError(
        data=data,
        fields_to_update=fields_to_update,
    )
