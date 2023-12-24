from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from authentification.models import UserProfile
from .form import FormCom,FormDisc
from .models import Discution,Communiquer
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from django.http import Http404
import datetime
from authentification.views import getProfile
# Create your views here.




@login_required
def Communication(request):
    user = request.user
    first_name = ""
    obj = Communiquer.objects.all().order_by('-date')
    profile = UserProfile.objects.all()
    paginator = Paginator(obj, 10)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        for objs in obj:
            for profiles in profile:
                if objs.user.username == profiles.user.username:
                    first_name = profiles.first_name
            
        form = FormCom()
        if request.method == "POST":
            form = FormCom(data=request.POST) 
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                form = FormCom()
                messages.success(request,"Le communiqué a été envoyé avec succès")
            else:
                messages.error(request, form.errors)
        
            
        context = {
            'username': user.username,
            'fisrt_name': first_name,
            'form': form,
            'obj':  page_obj,
            'profile': getProfile(request)['profile-admin']
        }
    except:
        raise Http404
   
    return render(request, 'Communiquer.html', context)

@login_required
def DiscutionFunc(request):
    user = request.user
    obj = Discution.objects.all().distinct() 
        
        #try:
    try:
        form = FormDisc
        if request.method == "POST":
                form = FormDisc(data=request.POST) 
                if form.is_valid():
                    form = form.save(commit=False)
                    form.user = request.user
                    form.save()
                    form = FormDisc()
                    messages.success(request,"")
                else:
                    messages.error(request, form.errors)
        context = {
                'form': form,
                'obj': obj,
                'profile': getProfile(request),
                'profile_admin': getProfile(request)['profile-admin'],
                'profile_disc': getProfile(request)['obj-profile'],
                'message': getProfile(request)['obj-message'],
            }
    except:
            raise Http404
        
    #except Discution.DoesNotExist:
    return render(request, 'Discution.html', context)

