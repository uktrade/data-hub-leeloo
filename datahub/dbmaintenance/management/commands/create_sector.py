from logging import getLogger

import reversion

from datahub.dbmaintenance.management.base import CSVBaseCommand
from datahub.dbmaintenance.utils import parse_limited_string, parse_uuid
from datahub.metadata.models import Sector, SectorCluster


logger = getLogger(__name__)


class Command(CSVBaseCommand):
    """Command to create a new Sector object."""

    def _process_row(self, row, simulate=False, **options):
        """Process one single row."""
        pk = parse_uuid(row['id'])
        segment = parse_limited_string(row['segment'])
        sector_cluster = parse_limited_string(row['sector_cluster'], max_length=None)
        parent_pk = parse_uuid(row['parent_id'])

        sector = Sector(pk=pk, segment=segment)

        if simulate:
            return

        if sector_cluster:
            sector_cluster_obj, _ = SectorCluster.objects.get_or_create(name=sector_cluster)
            sector.sector_cluster = sector_cluster_obj
        if parent_pk:
            sector.parent = Sector.objects.get(pk=parent_pk)

        with reversion.create_revision():
            sector.save(update_fields=('segment',))
            reversion.set_comment('Sector creation.')
