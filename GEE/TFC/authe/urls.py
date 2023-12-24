from django.urls import path
from .views import Login
app_name = 'accounts'

urlpatterns = [
    path('', Login, name='login')
]
