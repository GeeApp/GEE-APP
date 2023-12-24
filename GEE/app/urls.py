from django.urls import path
from .views import UpdateApp,Logo, CreateStudent,Palmares,AppartClasseStudent,PasseCreate,Edition,CoursCreate,ListeEleveEnsPalma,EpreuveCreate,OptionCreate,Search,EleveUpdateviews, DeleteEleve,ClassCreate
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = "app"
urlpatterns = [
    path('logo', Logo, name="logo"),
    path('updateApp', UpdateApp, name="updateApp"),
    path('createStudent', CreateStudent.as_view() , name="create_student"),
    path('appartclasse', AppartClasseStudent.as_view(), name="appartclasse"),
    path('listeleve', ListeEleveEnsPalma, name="liste_eleve") ,
    path('searchStudent', Search, name="searchStudent"),
    path('update_eleve/<int:pk>', EleveUpdateviews.as_view(), name='eleve_update'),
    path('delete_eleve/<int:id>', DeleteEleve, name='suppression'),
    ##-----------CLASSE-----------
    path('classecreate', ClassCreate.as_view() , name="create_classe"),
    ##-----------OPTION-----------
    path('Creationoption', OptionCreate.as_view() , name="create_option"),
    ##-----------EPREUVE-----------
    path('epreuvecreate', EpreuveCreate.as_view() , name="create_epreuve"),
    ##-----------COURS-----------
    path('courscreate', CoursCreate.as_view() , name="create_cours"),
     ##-----------PASSER-----------
    path('passecreate', PasseCreate.as_view() , name="create_passe"),
     ##-----------EDITION-----------
    path('edition', Edition , name="edition_liste"),
     ##-----------PROCLAMATION-----------
    path('proclamation', Palmares , name="proclamation"),
]

urlpatterns += staticfiles_urlpatterns()
