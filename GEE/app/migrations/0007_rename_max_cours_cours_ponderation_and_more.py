# Generated by Django 4.0.10 on 2023-11-24 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_passer_periode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cours',
            old_name='max_cours',
            new_name='Ponderation',
        ),
        migrations.RemoveField(
            model_name='cours',
            name='classe',
        ),
    ]