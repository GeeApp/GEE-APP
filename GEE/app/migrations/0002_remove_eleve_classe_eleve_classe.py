# Generated by Django 4.0.10 on 2023-09-26 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eleve',
            name='classe',
        ),
        migrations.AddField(
            model_name='eleve',
            name='classe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.classe'),
        ),
    ]
