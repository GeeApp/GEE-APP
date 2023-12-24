from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Promotion)
class AdminClasse(admin.ModelAdmin):
    list_display = ('CodeProm','LibProm')
    

@admin.register(Section)
class AdminClasse(admin.ModelAdmin):
    list_display = ('CodeSec','LibSec')



