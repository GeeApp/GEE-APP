from .models import *
from django import forms
from .models import Classe
from django.contrib.admin.widgets import FilteredSelectMultiple

#------------ELEVE------------------
class EleveForm(forms.ModelForm):
      sexe_choice = (
          ("M", "MASCULIN"),
          ("F", "FEMININ")
      )
      matr_eleve = forms.CharField(label='Matricule Elève', widget=forms.TextInput(
            attrs={
              'class': 'form-control ',
            }), required=True)
      nom_el = forms.CharField(label='nom', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      post_nom_el = forms.CharField(label='Post-Nom', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      prenom_el = forms.CharField(label='Prenom', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      date_nais_el = forms.CharField(label='Date-naissance', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
              'type': 'Date',
            }), required=True)
      sexe_el = forms.ChoiceField( widget=forms.Select(
            attrs={
              'class': 'form-control    my-2',
            }), choices=sexe_choice )
      nom_titeur = forms.CharField(label='Nom-Titeur', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      classe = forms.Select()
      Adress_el = forms.CharField(label='Adresse', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }))
      Tel_titeur = forms.CharField(label='Numéro-Titeur', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      
      
      class Meta:
            model = Eleve
            fields = '__all__'

#----------------------APPARTENIR--------------------------
class AppartClassForm(forms.ModelForm):
     
      anne_scol = forms.CharField(label='Année-Scolaire', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      
      class Meta:
            model = Appartenir
            fields = '__all__'
            
#------------------------CLASSE--------------------------
class ClassCreateForm(forms.ModelForm):
      code_class = forms.CharField(label='Code-classe', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      lib_class = forms.CharField(label='Libellé-classe', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      class Meta:
            model = Classe
            fields = '__all__'
            
#------------------------OPTION--------------------------
class OptionCreateForm(forms.ModelForm):
      code_opt = forms.CharField(label='Code-option', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      lib_opt = forms.CharField(label='Libellé-option', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      class Meta:
            model = Option
            fields = '__all__'

            
#------------------------EPREUVE--------------------------
class EpreuveCreateForm(forms.ModelForm):
      code_epr = forms.CharField(label='Code-épreuve', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      Lib_epr = forms.CharField(label='libellé-épreuve', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      max_epr = forms.CharField(label='Max', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      
      
      class Meta:
            model = Epreuve
            fields = '__all__'
            
#------------------------COURS--------------------------
class CoursCreateForm(forms.ModelForm):
      code_cours =  forms.CharField(label="Code-Cours", widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      lib_cours =  forms.CharField(label="Nom-Cours", widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }), required=True)
      Ponderation = forms.IntegerField(label="Pondération", widget=forms.TextInput(
            attrs={
              'class': 'form-control',
              'type': 'number',
            }), required=True)
      
      class Meta:
            model = Cours
            fields = '__all__'

class PasserCreateForm(forms.ModelForm):
    eleve_pas = forms.Select()
    epreuve_pas = forms.Select()
    cours_pas = forms.Select()
    date_pass = forms.CharField(label="Date",  widget=forms.TextInput(
            attrs={
              'class': 'form-control',
              'type': 'date',
              
            }), required=True)
    point_obt =forms.IntegerField(label="Point-Obtenu",  widget=forms.TextInput(
            attrs={
              'class': 'form-control',
              'type': 'number',
            }), required=True)
    periode =  forms.Select()
    semestre =  forms.Select()
      
    class Meta:
            model = Passer
            fields = '__all__'