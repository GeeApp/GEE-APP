from django.contrib import admin
from .models import Communiquer,Discution
# Register your models here.

class AdminProfile(admin.ModelAdmin):
     list_display = ('user','title', 'date', 'message')

class AdminDiscution (admin.ModelAdmin):
     list_display = ['user','message','date']
     
admin.site.register(Discution, AdminDiscution)     
admin.site.register(Communiquer, AdminProfile)
