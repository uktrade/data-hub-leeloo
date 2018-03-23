from rest_framework import serializers

from ..serializers import (
    RelaxedDateTimeField,
    SearchSerializer,
    SingleOrListField,
    StringUUIDField,
)


class SearchInteractionSerializer(SearchSerializer):
    """Serialiser used to validate interaction search POST bodies."""

    kind = SingleOrListField(child=serializers.CharField(), required=False)
    company = SingleOrListField(child=StringUUIDField(), required=False)
    company_name = serializers.CharField(required=False)
    contact = SingleOrListField(child=StringUUIDField(), required=False)
    contact_name = serializers.CharField(required=False)
    date_after = RelaxedDateTimeField(required=False)
    date_before = RelaxedDateTimeField(required=False)
    created_on_exists = serializers.BooleanField(required=False)
    dit_adviser = SingleOrListField(child=StringUUIDField(), required=False)
    dit_adviser_name = serializers.CharField(required=False)
    dit_team = SingleOrListField(child=StringUUIDField(), required=False)
    communication_channel = SingleOrListField(child=StringUUIDField(), required=False)
    investment_project = SingleOrListField(child=StringUUIDField(), required=False)
    service = SingleOrListField(child=StringUUIDField(), required=False)
    sector_descends = SingleOrListField(child=StringUUIDField(), required=False)

    DEFAULT_ORDERING = 'date:desc'

    SORT_BY_FIELDS = (
        'company.name',
        'contact.name',
        'date',
        'dit_adviser.name',
        'dit_team.name',
        'id',
        'subject',
    )
