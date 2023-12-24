# Generated by Django 4.0.10 on 2023-12-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='CodeProm',
            field=models.CharField(max_length=30, verbose_name='Code-Prom'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='LibProm',
            field=models.CharField(max_length=50, verbose_name='Libéllé-Prom'),
        ),
        migrations.AlterField(
            model_name='section',
            name='CodeSec',
            field=models.CharField(max_length=30, verbose_name='Code-Sec'),
        ),
        migrations.AlterField(
            model_name='section',
            name='LibSec',
            field=models.CharField(max_length=50, verbose_name='Libéllé-SeC'),
        ),
    ]