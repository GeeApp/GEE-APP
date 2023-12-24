from django.contrib import admin
from .models import UserProfile
# Register your models here.

class AdminProfile(admin.ModelAdmin):
     list_display = ('user', 'first_name', 'last_name' ,  'city', 'phone', 'image_parent')
admin.site.register(UserProfile, AdminProfile)