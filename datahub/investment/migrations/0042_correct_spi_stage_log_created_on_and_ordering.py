# Generated by Django 2.0.3 on 2018-03-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0041_add_spi_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investmentprojectstagelog',
            options={'ordering': ('created_on',)},
        ),
        migrations.AlterField(
            model_name='investmentprojectstagelog',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]
