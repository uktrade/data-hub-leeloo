# Generated by Django 2.2 on 2019-04-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0024_populate_other_contexts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='sector',
            name='lft',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='sector',
            name='rght',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
