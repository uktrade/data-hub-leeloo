# Generated by Django 2.0.7 on 2018-08-08 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20170807_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='av_reason',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='bucket_id',
            field=models.CharField(default='default', max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='status',
            field=models.CharField(choices=[('not_virus_scanned', 'Not virus scanned'), ('virus_scanning_scheduled', 'Virus scanning scheduled'), ('virus_scanning_in_progress', 'Virus scanning in progress'), ('virus_scanning_failed', 'Virus scanning failed.'), ('virus_scanned', 'Virus scanned'), ('deletion_pending', 'Deletion pending')], default='not_virus_scanned', max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('bucket_id', 'path')},
        ),
    ]
