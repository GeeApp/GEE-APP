# Generated by Django 4.0.10 on 2023-10-31 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_alter_discution_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discution',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 31, 12, 36, 5, 627805)),
        ),
    ]
