# Generated by Django 2.1 on 2018-08-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposition', '0004_update_permissions_django_21'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposition',
            name='details',
            field=models.TextField(blank=True),
        ),
    ]
