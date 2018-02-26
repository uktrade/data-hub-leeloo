import uuid

import reversion

from datahub.company.models import Company
from ..base import CSVBaseCommand


class Command(CSVBaseCommand):
    """Command to update Company.headquarter_type."""

    def add_arguments(self, parser):
        """Define extra arguments."""
        super().add_arguments(parser)
        parser.add_argument(
            '--simulate',
            action='store_true',
            dest='simulate',
            default=False,
            help='If True it only simulates the command without saving the changes.',
        )

    def _should_update(self, company, headquarter_type_id):
        return company.headquarter_type_id != headquarter_type_id

    def _process_row(self, row, simulate=False, **options):
        """Process one single row."""
        company = Company.objects.get(pk=row['id'])
        headquarter_type_id = _parse_uuid(row['headquarter_type_id'])

        if self._should_update(company, headquarter_type_id):
            company.headquarter_type_id = headquarter_type_id

            if simulate:
                return

            with reversion.create_revision():
                company.save(
                    update_fields=(
                        'headquarter_type',
                    )
                )
                reversion.set_comment('Headquarter type data migration correction.')


def _parse_uuid(id_):
    if not id_ or id_.lower().strip() == 'null':
        return None
    return uuid.UUID(id_)
