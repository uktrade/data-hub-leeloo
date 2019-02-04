# Generated by Django 2.1.5 on 2019-01-31 20:13

from logging import getLogger

from django.db import migrations
from django.db.models import (
    BooleanField,
    Case,
    ExpressionWrapper,
    Q,
    Subquery,
    Value,
    When,
)
from django.db.models.functions import Coalesce

logger = getLogger(__name__)


def populate_company_address_fields(apps, schema_editor):
    """
    Populates company address fields from trading address or registered address
    whichever is defined.
    """
    company_model = apps.get_model('company', 'Company')

    # Coalesce makes sure that both NULL and '' values are treated equally
    base_queryset = company_model.objects.annotate(
        address_1_normalised=Coalesce('address_1', Value('')),
        address_town_normalised=Coalesce('address_town', Value('')),
        trading_address_1_normalised=Coalesce('trading_address_1', Value('')),
        trading_address_town_normalised=Coalesce('trading_address_town', Value('')),
        registered_address_1_normalised=Coalesce('registered_address_1', Value('')),
        registered_address_2_normalised=Coalesce('registered_address_2', Value('')),
        registered_address_town_normalised=Coalesce('registered_address_town', Value('')),
        registered_address_county_normalised=Coalesce('registered_address_county', Value('')),
        registered_address_postcode_normalised=Coalesce('registered_address_postcode', Value('')),
        has_valid_trading_address=ExpressionWrapper(
            ~Q(trading_address_1_normalised='')
            & ~Q(trading_address_town_normalised='')
            & Q(trading_address_country__isnull=False),
            output_field=BooleanField(),
        ),
        has_registered_address=ExpressionWrapper(
            ~Q(registered_address_1_normalised='')
            | ~Q(registered_address_2_normalised='')
            | ~Q(registered_address_town_normalised='')
            | ~Q(registered_address_postcode_normalised='')
            | ~Q(registered_address_county_normalised='')
            | Q(registered_address_country__isnull=False),
            output_field=BooleanField(),
        ),
    )

    subquery = base_queryset.filter(
        Q(has_registered_address=True) | Q(has_valid_trading_address=True),
        address_1_normalised='',
        address_town_normalised='',
        address_country__isnull=True,
    ).values(
        'pk',
    )

    num_updated = base_queryset.filter(
        pk__in=Subquery(subquery),
    ).update(
        address_1=Case(
            When(has_valid_trading_address=True, then='trading_address_1'),
            default='registered_address_1',
        ),
        address_2=Case(
            When(has_valid_trading_address=True, then='trading_address_2'),
            default='registered_address_2',
        ),
        address_town=Case(
            When(has_valid_trading_address=True, then='trading_address_town'),
            default='registered_address_town',
        ),
        address_county=Case(
            When(has_valid_trading_address=True, then='trading_address_county'),
            default='registered_address_county',
        ),
        address_postcode=Case(
            When(has_valid_trading_address=True, then='trading_address_postcode'),
            default='registered_address_postcode',
        ),
        address_country=Case(
            When(has_valid_trading_address=True, then='trading_address_country'),
            default='registered_address_country',
        ),
    )

    logger.info(f'Populated {num_updated} company addresses')


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0062_add_address'),
    ]

    operations = [
        migrations.RunPython(populate_company_address_fields, migrations.RunPython.noop, elidable=True)
    ]
