# Generated by Django 4.0.10 on 2023-09-26 10:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=350)),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 9, 26, 12, 39, 59, 360823))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Discution',
                'verbose_name_plural': 'Discutions',
            },
        ),
        migrations.CreateModel(
            name='Communiquer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('date', models.DateField(auto_now=True)),
                ('message', models.CharField(default='', max_length=350)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Communiquer',
                'verbose_name_plural': 'Communiquers',
            },
        ),
    ]