# Generated by Django 4.0.10 on 2023-11-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_max_cours_cours_ponderation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='epreuve',
            name='max_epr',
            field=models.CharField(blank=True, max_length=3, verbose_name='Max-Epreuve'),
        ),
        migrations.AlterField(
            model_name='cours',
            name='Ponderation',
            field=models.IntegerField(verbose_name='Pondération'),
        ),
        migrations.AlterField(
            model_name='epreuve',
            name='Lib_epr',
            field=models.CharField(max_length=5, verbose_name='Libéllé-Epreuve'),
        ),
        migrations.AlterField(
            model_name='epreuve',
            name='code_epr',
            field=models.CharField(max_length=5, verbose_name='Code-Epreuve'),
        ),
    ]
