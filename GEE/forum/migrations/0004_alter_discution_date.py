# Generated by Django 4.0.10 on 2023-10-11 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_discution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discution',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 11, 16, 13, 10, 602759)),
        ),
    ]
