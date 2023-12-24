from django.db import models
from django.contrib.auth.models import User
from django.urls  import reverse
# Create your models here.
class UserProfile(models.Model): 
   
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name='profile')
    first_name = models.CharField("Nom",max_length=225, default='')
    last_name = models.CharField("Post_nom",max_length=225, default='')
    city = models.CharField("ville",max_length=225, default='K')
    phone = models.CharField("Phone",max_length=20, default='')
    image_parent = models.ImageField( upload_to='post_image/', blank=True, default='')
    
    
    def __str__(self):
        return self.first_name
    