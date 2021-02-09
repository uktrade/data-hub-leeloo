from datetime import date

from django.db.models import Case, Count, F, Q, When
from django.db.models.functions import Coalesce, Extract
from django.utils import timezone
from rest_framework import serializers

from datahub.company.models import Advisor
from datahub.core.constants import InvestmentProjectStage
from datahub.core.utils import get_financial_year
from datahub.investment.project.models import InvestmentProject


class AdvisorIProjectSummarySerializer(serializers.Serializer):
    """
    Serializer for Investment Project Summaries.
    """

    annual_summaries = serializers.SerializerMethodField(read_only=True)
    adviser_id = serializers.UUIDField(source='id')

    class Meta:
        model = Advisor

    def get_annual_summaries(self, obj):
        """
        Gets annual summaries for the current and previous financial years.
        """
        current_financial_year = get_financial_year(timezone.now())
        start_year = current_financial_year - 1
        end_year = current_financial_year + 1

        # Get any projects where this adviser is involved
        projects = InvestmentProject.objects.filter(
            Q(client_relationship_manager__id=obj.id)
            | Q(project_assurance_adviser__id=obj.id)
            | Q(project_manager__id=obj.id)
            | Q(team_members__id=obj.id),
        )

        prospect_count = projects.filter(
            stage=InvestmentProjectStage.prospect.value.id,
        ).count()

        project_summaries = (
            projects.annotate(
                land_date=Coalesce('actual_land_date', 'estimated_land_date'),
                land_date_year=Extract('land_date', 'year'),
                land_date_month=Extract('land_date', 'month'),
                financial_year=Case(
                    When(land_date_month__gte=4, then=F('land_date_year')),
                    default=F('land_date_year') - 1,
                ),
            )
            .exclude(stage=InvestmentProjectStage.prospect.value.id)
            .filter(financial_year__gte=start_year, financial_year__lt=end_year)
            .values('financial_year', 'stage', 'stage__name')
            .annotate(count=Count('stage'))
            .order_by('financial_year')
        )

        results = {}
        for financial_year in reversed(range(start_year, end_year)):
            results[financial_year] = {
                'financial_year': {
                    'label': f'{financial_year}-{str(financial_year + 1)[-2:]}',
                    'start': date(year=financial_year, month=4, day=1),
                    'end': date(year=financial_year + 1, month=3, day=31),
                },
                'totals': {
                    InvestmentProjectStage.prospect.name: {
                        'label': 'Prospect',
                        'id': InvestmentProjectStage.prospect.value.id,
                        'value': prospect_count,
                    },
                    InvestmentProjectStage.assign_pm.name: {
                        'label': 'Assigned',
                        'id': InvestmentProjectStage.assign_pm.value.id,
                        'value': 0,
                    },
                    InvestmentProjectStage.active.name: {
                        'label': 'Active',
                        'id': InvestmentProjectStage.active.value.id,
                        'value': 0,
                    },
                    InvestmentProjectStage.verify_win.name: {
                        'label': 'Verify Win',
                        'id': InvestmentProjectStage.verify_win.value.id,
                        'value': 0,
                    },
                    InvestmentProjectStage.won.name: {
                        'label': 'Won',
                        'id': InvestmentProjectStage.won.value.id,
                        'value': 0,
                    },
                },
            }

        for project_summary in project_summaries:
            year = project_summary['financial_year']
            stage = InvestmentProjectStage.get_by_id(project_summary['stage'])
            if stage is not None and stage.name in results[year]['totals']:
                results[year]['totals'][stage.name]['value'] = project_summary['count']

        return list(results.values())
