from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404,HttpResponse
import uuid
from django.views import View
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import UserForm,UserFormUpdate
from .models import UserProfile
from forum.models import Discution
#from ..app.verif_perms import *
from django.urls import reverse_lazy
# Create your views here.
def Is_Enseignants(user):
    if user.groups.filter(name = 'Enseignants').exists():
        update = """ Mise à jour"""
        return  update
       

def Register(request):
    #CREATE ACCOUNT
    data = request.POST
    form = UserForm

    try :
        if request.method == 'POST':
        
            username = data['username']
            email = data['email']
            password = data['password1']
            re_passowrd = data['password2']
            
            user = User.objects.filter(email=email).filter()   
           
            if user:
              messages.error(request, 'Cette adresse mail éxiste déjà')
              return redirect('accounts:Register')
        
            user = User.objects.filter(username=username)
            if user:
               messages.error(request, "Ce nom d'utilisateur existe déjà")
               return redirect('accounts:Register')
        
            if not password == re_passowrd:
               messages.error(request, 'Veullez confirmer le mot de passe')
               return redirect('accounts:Register')

            if  len(password) < 8:
                messages.error(request, 'Votre mot de passe est trop court. il doit contenir 8 caractère au moin ')
                return redirect('accounts:Register')
        
        form = UserForm(data=request.POST)
        if form.is_valid():
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                user = User.objects.get(id=user.id)
                user_profile = UserProfile.objects.create(user=user, first_name='', last_name='',  city='', phone='', image_parent='')
                user_profile.save()
            
                return redirect('accounts:Login')
        else:
                messages.error(request, 'Votre mot de passe doit contenir des lettres et des chiffres ou carectère spéciaux')
        
        context = {
            'form': form
        }   
    except Exception as e:
       return e
   
    return render(request,'account/register.html', context)

def Login(request):
    #PAGE CONNEXION
    user = request.user
   
    try:     
            if request.method == "POST":
                data = request.POST
                username = data['username']
                password = data['password']
                    
                if not username or not password:
                    messages.error(request, 'Veuillez remplire tous les champs')
                    return redirect('accounts:Login')
                
                obj = User.objects.filter(username=username).first
                
                if obj is None:
                    messages.error(request, 'Utilisateur non trouvé')
                
                user = authenticate(username = username, password = password)
                if user is None:
                    messages.error(request, "Erreur d'authentification")
                    return redirect('accounts:Login')
                login(request, user)
                
                return redirect('accounts:Home')
    except:  
        return messages.error(request,'Une erreur est survenue')
        
    return render(request,'account/Login.html')

@login_required
def deconnexion(request):
    if request.method == 'GET':
        logout(request)
    return redirect('accounts:Login')

@login_required
def Home(request):
  
    
    context = {
        'update': Is_Enseignants(request.user)
    }
    return render(request, 'pages/Home.html', context)


def getProfile(request):
    profile = UserProfile.objects.get(user=request.user.id)
    user = User.objects.all()
    profile_post_discu = Discution.objects.all()
    context = {}
    profile_admin = None
    profile_disc= UserProfile.objects.all()
    message = None
    image = None
    
    try:
        for users in user:
            if users.is_superuser: 
                profile_admin = UserProfile.objects.get(user=users.pk)
    
        for prof_disc in profile_post_discu:
            for prf in profile_disc:
                if prof_disc.user.pk == prf.user.pk:
                    image = prf
                    
    
        context = {
            'profile_user_connected': profile.image_parent,
            'profile-admin': profile_admin.image_parent,
            'profile-disc': image,
            'obj-profile':  profile_disc,
            'obj-message': profile_post_discu 
        }
    except:
        raise Http404
   
    return context

@login_required
def update_profile(request, id):
   profile = UserProfile.objects.get(user=id)
   
   try:
       form =  UserFormUpdate()
       if request.method ==  "POST":
            form = UserFormUpdate(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form = form.save()
                form = UserFormUpdate
        
       context = {
            'form': form,
            'profile': getProfile(request)['profile_user_connected'],
            'update': Is_Enseignants(request.user)
        }  
   except: 
       raise Http404
   
   return render(request, 'account/update_profile.html', context)

