# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 09:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('investment', '0001_squash_0007_initial'), ('investment', '0002_rename_advsor_fkeys_to_adviser'), ('investment', '0003_add_investment_archiving'), ('investment', '0004_investment_tidy_up'), ('investment', '0005_add_evaluation_fields'), ('investment', '0006_add_investemnt_document'), ('investment', '0007_rename_phase_to_stage'), ('investment', '0007_fix_doc_type'), ('investment', '0008_merge_20170707_0824'), ('investment', '0009_add_likelihood_priority'), ('investment', '0010_add_team_members'), ('investment', '0011_add_fdi_value'), ('investment', '0012_add_additional_fields'), ('investment', '0013_add_quotable_as_case_study')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_squash_0030_initial'),
        ('metadata', '0003_add_fdi_value'),
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentProject',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('nda_signed', models.BooleanField()),
                ('estimated_land_date', models.DateField()),
                ('cdms_project_code', models.CharField(blank=True, max_length=255, null=True)),
                ('project_shareable', models.NullBooleanField()),
                ('not_shareable_reason', models.TextField(blank=True, null=True)),
                ('referral_source_activity_event', models.CharField(blank=True, max_length=255, null=True)),
                ('client_cannot_provide_total_investment', models.NullBooleanField()),
                ('total_investment', models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True)),
                ('client_cannot_provide_foreign_investment', models.NullBooleanField()),
                ('foreign_equity_investment', models.DecimalField(blank=True, decimal_places=0, max_digits=19, null=True)),
                ('government_assistance', models.NullBooleanField()),
                ('number_new_jobs', models.IntegerField(blank=True, null=True)),
                ('number_safeguarded_jobs', models.IntegerField(blank=True, null=True)),
                ('r_and_d_budget', models.NullBooleanField()),
                ('non_fdi_r_and_d_budget', models.NullBooleanField()),
                ('new_tech_to_uk', models.NullBooleanField()),
                ('export_revenue', models.NullBooleanField()),
                ('client_requirements', models.TextField(blank=True, null=True)),
                ('site_decided', models.NullBooleanField()),
                ('address_line_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_3', models.CharField(blank=True, max_length=255, null=True)),
                ('address_line_postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('client_considering_other_countries', models.NullBooleanField()),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('average_salary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='metadata.SalaryRange')),
                ('business_activities', models.ManyToManyField(blank=True, related_name='_investmentproject_business_activities_+', to='metadata.InvestmentBusinessActivity')),
                ('client_contacts', models.ManyToManyField(blank=True, related_name='investment_projects', to='company.Contact')),
                ('client_relationship_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to=settings.AUTH_USER_MODEL)),
                ('competitor_countries', models.ManyToManyField(blank=True, related_name='_investmentproject_competitor_countries_+', to='metadata.Country')),
                ('fdi_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to='metadata.FDIType')),
                ('intermediate_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intermediate_investment_projects', to='company.Company')),
                ('investment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='investment_projects', to='metadata.InvestmentType')),
                ('investor_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='investor_investment_projects', to='company.Company')),
                ('non_fdi_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to='metadata.NonFDIType')),
                ('stage', models.ForeignKey(default='8a320cc9-ae2e-443e-9d26-2f36452c2ced', on_delete=django.db.models.deletion.PROTECT, related_name='investment_projects', to='metadata.InvestmentProjectStage')),
                ('project_assurance_adviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('project_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('referral_source_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to='metadata.ReferralSourceActivity')),
                ('referral_source_activity_marketing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to='metadata.ReferralSourceMarketing')),
                ('referral_source_activity_website', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to='metadata.ReferralSourceWebsite')),
                ('referral_source_adviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='referred_investment_projects', to=settings.AUTH_USER_MODEL)),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='metadata.Sector')),
                ('strategic_drivers', models.ManyToManyField(blank=True, related_name='investment_projects', to='metadata.InvestmentStrategicDriver')),
                ('uk_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investee_projects', to='company.Company')),
                ('uk_region_locations', models.ManyToManyField(blank=True, related_name='_investmentproject_uk_region_locations_+', to='metadata.UKRegion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestmentProjectCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='investment.InvestmentProject')),
            ],
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='archived_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='archived_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='archived_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='actual_land_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='approved_commitment_to_invest',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='approved_fdi',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='approved_good_value',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='approved_high_value',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='approved_landed',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='approved_non_fdi',
            field=models.NullBooleanField(),
        ),
        migrations.CreateModel(
            name='IProjectDocument',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('archived_on', models.DateTimeField(blank=True, null=True)),
                ('archived_reason', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('doc_type', models.CharField(choices=[('actual_land_date', 'Actual land date'), ('hq', 'Global/European HQ evidence'), ('foreign_ownership', 'Foreign ownership evidence'), ('operations_commenced', 'Operations commenced'), ('total_investment', 'Total investment'), ('foreign_equity_investment', 'Foreign equity investment'), ('number_new_jobs', 'Number new jobs'), ('number_safeguarded_jobs', 'Number safeguarded jobs'), ('r_and_d_budget', 'R and D budget'), ('new_tech_to_uk', 'New tech to uk'), ('export_revenue', 'Export revenue'), ('average_salary', 'Average salary')], max_length=255)),
                ('filename', models.CharField(max_length=255)),
                ('archived_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='documents.Document')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='investment.InvestmentProject')),
            ],
            options={
                'verbose_name': 'investment project document',
                'verbose_name_plural': 'investment project documents',
            },
        ),
        migrations.AlterUniqueTogether(
            name='iprojectdocument',
            unique_together=set([('project', 'doc_type', 'filename')]),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='likelihood_of_landing',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='priority',
            field=models.CharField(blank=True, choices=[('1_low', 'Low'), ('2_medium', 'Medium'), ('3_high', 'High')], max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='InvestmentProjectTeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('adviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('investment_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='investment.InvestmentProject')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='investmentprojectteammember',
            unique_together=set([('investment_project', 'adviser')]),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='fdi_value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='investment_projects', to='metadata.FDIValue'),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='some_new_jobs',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='uk_company_decided',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='will_new_jobs_last_two_years',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='investmentproject',
            name='quotable_as_public_case_study',
            field=models.NullBooleanField(),
        ),
    ]
