from .models import Communiquer,Discution
from django import forms 
from django.contrib.auth.models import User

class FormCom(forms.ModelForm):

    title = forms.CharField(label="Titre",required=True, widget=forms.TextInput(
        attrs={
        'placeholder': 'Titre du communiquer',
          'class': 'form-control',
        }
    ))
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={
        'placeholder': 'passez votre le communiqué',
        'class': 'form-control',
        'rows': 5,
        'cols': 25,
        }
    ))
    class Meta:
        model = Communiquer
        fields = ('title','message',)
        

class FormDisc(forms.ModelForm):
    
    message = forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={
        'placeholder': 'Votre message...',
        'class': 'form-control',
        'rows': 5,
        'cols': 25,
        }
    ))
    class Meta:
        model = Discution
        fields = ('message',)
        
