from django.db import models

# Create your models here.

class Section(models.Model):
    CodeSec = models.CharField("Code-Sec", blank=False,max_length=30)
    LibSec = models.CharField("Libéllé-SeC", blank=False,max_length=50)


class Promotion(models.Model):
    CodeProm = models.CharField("Code-Prom", blank=False,max_length=30)
    LibProm = models.CharField("Libéllé-Prom", blank=False,max_length=50)
    
    