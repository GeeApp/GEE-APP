# Generated by Django 4.0.10 on 2023-11-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_cours_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epreuve',
            name='Lib_epr',
            field=models.CharField(max_length=40, verbose_name='Libéllé-Epreuve'),
        ),
    ]
