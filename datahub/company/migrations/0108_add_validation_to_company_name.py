# Generated by Django 3.1.6 on 2021-02-16 17:22

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0107_remove_accepts_dit_email_marketing_from_django'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^[=+-@]'), code='invalid', inverse_match=True, message='Enter a valid name')]),
        ),
    ]
