# Generated by Django 4.0.10 on 2023-12-07 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0026_alter_discution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discution',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 20, 21, 58, 830034)),
        ),
    ]
