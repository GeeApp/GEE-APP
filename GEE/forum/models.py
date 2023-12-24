from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Communiquer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=50, blank=False, default="")
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=350, blank=False,default="" )
    
     
    class Meta:
        verbose_name = ("Communiquer")
        verbose_name_plural = ("Communiquers")
    
    def __str__(self):
        return self.title

class Discution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=350, blank=False,default="" )
    date = models.DateTimeField( default=datetime.datetime.now())
    
    class Meta:
        verbose_name = ("Discution")
        verbose_name_plural = ("Discutions")
    
    def __str__(self):
        return self.user.username