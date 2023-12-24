# Generated by Django 4.0.10 on 2023-09-26 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_class', models.CharField(max_length=50, verbose_name='Code-Classe')),
                ('lib_class', models.CharField(max_length=20, verbose_name='Libellé-Classe')),
            ],
            options={
                'verbose_name': 'Classe',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_cour', models.CharField(max_length=30, verbose_name='Code-Cours')),
                ('lib_cours', models.CharField(max_length=100, verbose_name='Nom-Cours')),
                ('max_cours', models.IntegerField(verbose_name='Maximum-Cours')),
                ('classe', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matr_eleve', models.CharField(max_length=30, verbose_name='Matricule')),
                ('nom_el', models.CharField(max_length=30, verbose_name='Nom-Elève')),
                ('post_nom_el', models.CharField(default='', max_length=30, verbose_name='Post-Nom-Elève')),
                ('prenom_el', models.CharField(default='', max_length=30, verbose_name='Prenom-Elève')),
                ('date_nais_el', models.CharField(default='', max_length=30, verbose_name='Date-naissance-Elève')),
                ('sexe_el', models.CharField(default='M', max_length=1, verbose_name='Sexe Elève')),
                ('nom_titeur', models.CharField(default='', max_length=30, verbose_name='Nom-Titeur')),
                ('Adress_el', models.CharField(default='', max_length=30, verbose_name='Adresse-Elève')),
                ('Tel_titeur', models.CharField(default='', max_length=30, verbose_name='Numéro-tuteur')),
                ('classe', models.ManyToManyField(to='app.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Enseigant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ens', models.CharField(max_length=30, verbose_name='Nom-Enseignant')),
                ('matr_ens', models.CharField(max_length=30, verbose_name='Matricule-Enseignant')),
                ('post_ens', models.CharField(default='', max_length=30, verbose_name='Post-Nom-Enseigant')),
                ('prenom_ens', models.CharField(default='', max_length=30, verbose_name='Prenom-Enseigant')),
                ('date_nais_ens', models.CharField(default='', max_length=30, verbose_name='Date-Naissance-Enseigant')),
                ('sexe_ens', models.CharField(default='M', max_length=1, verbose_name='Sexe')),
                ('etat_civil_ens', models.CharField(default='C', max_length=1, verbose_name='Etat-Civil')),
                ('niveau_etude', models.CharField(max_length=30, verbose_name="Niveau-D'étude")),
                ('adresse_ens', models.CharField(default='', max_length=30, verbose_name='Adresse-Enseignant')),
                ('date_engagement', models.CharField(default='', max_length=30, verbose_name='Date-Engagement')),
                ('tel_ens', models.CharField(default='', max_length=30, verbose_name='Numéro-Enseigant')),
            ],
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_epr', models.CharField(max_length=30, verbose_name='Code-Epreuve')),
                ('Lib_epr', models.CharField(max_length=50, verbose_name='Libéllé-Epreuve')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_opt', models.CharField(max_length=50, verbose_name='Code-Option')),
                ('lib_opt', models.CharField(max_length=20, verbose_name='Libellé-Option')),
            ],
        ),
        migrations.CreateModel(
            name='Periode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_per', models.CharField(max_length=30, verbose_name='Code-Période')),
                ('lib_periode', models.CharField(max_length=50, verbose_name='Libéllé-Période')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_per', models.CharField(max_length=30, verbose_name='Code-Semestre')),
                ('lib_semestre', models.CharField(max_length=50, verbose_name='Libéllé-Semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Titulaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anne_scol', models.CharField(max_length=30, verbose_name='Année-Scolaire')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classe')),
                ('enseigant_titulaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.enseigant')),
            ],
        ),
        migrations.CreateModel(
            name='Passer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pass', models.CharField(max_length=30, verbose_name='Date')),
                ('point_obt', models.IntegerField(verbose_name='Point-Obtenu')),
                ('max_cours', models.IntegerField(verbose_name='Maximum-Epreuve')),
                ('cours_pas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cours')),
                ('eleve_pas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.eleve')),
                ('epreuve_pas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.epreuve')),
                ('periode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.periode')),
                ('semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semestre')),
            ],
        ),
        migrations.AddField(
            model_name='eleve',
            name='option',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.option'),
        ),
        migrations.CreateModel(
            name='Dispenser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anne_scol_disp', models.CharField(max_length=30, verbose_name='Année-Scolaire')),
                ('classe_disp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classe')),
                ('cours_disp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cours')),
                ('enseigant_disp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.enseigant')),
            ],
        ),
        migrations.CreateModel(
            name='Appartenir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anne_scol', models.CharField(max_length=30, verbose_name='Anne-Scolaire')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classe')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.eleve')),
            ],
        ),
    ]