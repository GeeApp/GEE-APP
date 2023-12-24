from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Classe)
class AdminClasse(admin.ModelAdmin):
    list_display = ('code_class','lib_class')
    search_fields = ['code_class',]


@admin.register(Option)
class AdminOption(admin.ModelAdmin):
    list_display = ('code_opt','lib_opt')
    search_fields = ['code_opt',]


@admin.register(Appartenir)
class AdminAppartenir(admin.ModelAdmin):
    list_display = ('anne_scol','eleve','classe')
    search_fields = ['anne_scol',]


@admin.register(Eleve)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('matr_eleve', 'nom_el', 'post_nom_el', 'prenom_el', 'date_nais_el', 'sexe_el', 'nom_titeur','classe','option', 'Adress_el', 'Tel_titeur')
    search_fields = ['matr_eleve',]

class AdminEpreuve(admin.ModelAdmin):
    list_display = ('code_epr','Lib_epr','max_epr')   
admin.site.register(Epreuve, AdminEpreuve)

@admin.register(Periode)
class AdminPeriod(admin.ModelAdmin):
    list_display = ('code_per','lib_periode')
    

@admin.register(Semestre)
class AdminSemestre(admin.ModelAdmin):
    list_display = ('code_sem','lib_sem')


@admin.register(Cours)
class AdminCours(admin.ModelAdmin):
    list_display = ('code_cours','lib_cours', 'Ponderation')


@admin.register(Passer)
class AdminPasser(admin.ModelAdmin):
    list_display = ('eleve_pas','epreuve_pas','cours_pas', 'date_pass','point_obt','periode','semestre')


@admin.register(Enseigant)
class AdminEnseignant(admin.ModelAdmin):
    list_display = ('nom_ens','matr_ens','post_ens','prenom_ens','sexe_ens','date_nais_ens','adresse_ens') 


@admin.register(Dispenser)
class AdminDispenser(admin.ModelAdmin):
    list_display = ('classe_disp','cours_disp','enseigant_disp','anne_scol_disp') 



@admin.register(Titulaire)
class AdminClasse(admin.ModelAdmin):
    list_display = ('enseigant_titulaire','classe','anne_scol')