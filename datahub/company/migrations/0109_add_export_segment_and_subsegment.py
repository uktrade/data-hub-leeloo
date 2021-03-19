# Generated by Django 3.1.7 on 2021-03-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0108_create_company_state_fk_base_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='export_segment',
            field=models.CharField(blank=True, choices=[(None, 'No export segment or not known'), ('hep', ' High export potential'), ('non-hep', 'Not high export potential')], default='', help_text='Segmentation of export', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='export_sub_segment',
            field=models.CharField(blank=True, choices=[(None, 'No sub export segment or not known'), ('sustain_nurture_and_grow', 'Sustain: nurture & grow'), ('sustain_develop_export_capability', 'Sustain: develop export Capability'), ('sustain_communicate_benefits', 'Sustain: communicate benefits'), ('sustain_increase_competitiveness', 'Sustain: increase competitiveness'), ('reassure_nurture_and_grow', 'Reassure: nurture & grow'), ('reassure_develop_export_capability', 'Reassure: develop export capability'), ('reassure_leave_be', 'Reassure: leave be'), ('reassure_change_the_game', 'Reassure: change the game'), ('promote_develop_export_capability', 'Promote: develop export capability'), ('promote_communicate_benefits', 'Promote: communicate benefits'), ('promote_change_the_game', 'Promote: change the game'), ('challenge', 'Challenge')], default='', help_text='Sub-Segmentation of export', max_length=255),
        ),
    ]
