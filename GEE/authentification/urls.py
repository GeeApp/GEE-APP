from django.urls import path
from .views import Login,Register,Home,deconnexion,update_profile 
app_name = 'accounts'

urlpatterns = [
    path('', Login, name='Login'),
    path('register', Register, name='Register'),
    path('logout', deconnexion, name='Logout'),
    path('home', Home, name='Home'),
    path('profile/<int:id>', update_profile, name='update_profile'),
    #path('update/<int:pk>/profile',  UpdateProfile.as_view(), name='update_profile')
]
