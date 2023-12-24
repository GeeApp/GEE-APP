from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.forms.widgets import Select

class UserForm(UserCreationForm):
      username = forms.CharField(label='Nom utilisateur', widget=forms.TextInput(
            attrs={
              'class': 'form-control',
            }))
      email = forms.CharField(label='Email', widget=forms.EmailInput(
            attrs={
              'class': 'form-control',
            }))
      password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
            attrs={
              'class': 'form-control',
            }))
      password2 = forms.CharField(label='confirme password', widget=forms.PasswordInput(
            attrs={
              'class': 'form-control',
            }))
     
      class Meta:
            model = User
            fields = ('id', 'username', 'email', 'password1', 'password2')


class UserFormUpdate(forms.ModelForm):
      Cyti_choise = ( ("K","Kishasa"),("M","Matadi"))
      
      first_name = forms.CharField(label='Nom', widget=forms.TextInput(
            attrs={
              'class': 'form-control p-3  my-2',
              'placeholder': 'Entrez votre nom...'
            }), required=True)
      last_name = forms.CharField(label='Post-nom', widget=forms.TextInput(
            attrs={
              'class': 'form-control p-3    my-2',
               'placeholder': 'Entrez votre Postnom...'
            }),required=True)
      city = forms.ChoiceField( widget=forms.Select(
            attrs={
              'class': 'form-control    my-2',
            }), choices=Cyti_choise )
      phone = forms.CharField(label='Téléphone', widget=forms.TextInput(
            attrs={
              'class': 'form-control p-3  my-2',
              'placeholder': 'Entrez votre numéro'
            }))
      image_parent = forms.FileField(label='Photo', widget=forms.FileInput(
            attrs={
              'class': 'form-control   my-2',
              'type': 'file'
            }),required=False)
     
      class Meta:
            model = UserProfile
            fields = ('first_name', 'last_name', 'city', 'phone', 'image_parent')

