from django.urls import path
from .views import Communication,DiscutionFunc

app_name = "forum"

urlpatterns = [
    path('communiquer/', Communication,name="communiquer"),
    path('discussion', DiscutionFunc, name="discussion"),
    #path('error404',error_http_404_views, name='error_404')
    
]