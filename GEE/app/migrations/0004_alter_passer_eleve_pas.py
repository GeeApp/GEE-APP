# Generated by Django 4.0.10 on 2023-10-31 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_passer_max_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passer',
            name='eleve_pas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.eleve', verbose_name='Eleve'),
        ),
    ]