# Generated by Django 4.0.10 on 2023-11-27 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_alter_discution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discution',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 22, 9, 36, 433748)),
        ),
    ]