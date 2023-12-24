from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from .forms import *
from .verif_perms import *
from django.http import Http404
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.views import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.

@login_required
@user_passes_test(Is_Enseignants)
def UpdateApp(request):
    
    return render(request, 'mise_ajour.html')

class CreateStudent(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = (
    'Eleve.can_add'
    )
    form = EleveForm()
    template_name = 'create-student.html'
    success_url = '/'
    error = ""
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = EleveForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("app:appartclasse")
        else:
            self.error = "Opération non réuissie"
        return render(request, self.template_name, {'errors': self.error, "form":self.form})


class AppartClasseStudent(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'Appartenir.can_add'
    template_name = 'appartenir.html'
    form_class = AppartClassForm
    queryset = Appartenir.objects.all()
    success_url = '/app/createStudent'
    
@user_passes_test(Is_Administration)
def ListeEleveEnsPalma(request):
    try:
        template_name = 'liste_eleve.html'
        context = {}
        if request.user.groups.filter(name = 'Administration').exists():
                eleve = Eleve.objects.all()[:10]
                ens =  Enseigant.objects.all().order_by('id')
                button = [request.GET.get('page'),request.GET.get('imprimer')]
       
                if button[0] == "impression_liste":
                    template_name = 'impression_liste.html' 
                    eleve = Eleve.objects.all().order_by('id')
                    
                    
                context = {
                'Eleve': eleve,
                'getLink': button[0],
                'liste': button[1],
                'Teacher': ens
                }    
    except:
        raise Http404
    return render(request,template_name,context) 



def Logo(request):
    
    return render(request)

class EleveUpdateviews(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'Eleve.can_change'
    form_class = EleveForm
    template_name = 'eleve_update.html'
    queryset = Eleve.objects.all()
    success_url = '/app/listeleve'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Eleve, pk=pk)
    
@login_required 
@permission_required('Eleve.can_delete', raise_exception= True)
def DeleteEleve(request, id):
    obj = get_object_or_404(Eleve, id=id)
    name =  obj.nom_el
    matr = obj.matr_eleve
       
    if request.method == "POST":
        obj.delete()
        return redirect('app:liste_eleve ?page=suppression')
    context = {
        'name': name,
        'matr' : matr
    }
    return render(request, 'suppression.html',context)

@login_required  
def Search(request):
    try:
        search = request.GET.get('search')
        student = Eleve.objects.filter(Q(matr_eleve__icontains=search) | Q(nom_el__icontains=search) | Q(post_nom_el__icontains=search) | Q(prenom_el__icontains=search))
        
        context = {
            'student': student
        }
        if not student:
            context['null']= "Aucun résultat n'a été trouivée pour cette recherche"
        elif student == None:
             context['null']= "Aucun résultat n'a été trouivée pour cette recherche"
    except:
       raise Http404
    return render(request, 'search.html', context)

#####-------Création Classe-----------
class ClassCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView): 
    permission_required = 'Classe.can_add'
    template_name = 'create-class.html'
    form_class = ClassCreateForm
    queryset = Classe.objects.all()
    success_url = '/app/classecreate'
    messages = ""
    
    def post(self, request, *args, **kwargs):
        form = ClassCreateForm(request.POST)
        if form.is_valid():
           form.save()
           form = ClassCreateForm()
           self.messages = "Opération réussie"
           print(self.messages)
        else:
            self.messages = "Opération non réuissie"
        return render(request, self.template_name, {'messages': self.messages, "form": form})    
    
#####-------Création option-----------
class OptionCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView): 
    permission_required = 'Option.can_add'
    template_name = 'create-option.html'
    form_class = OptionCreateForm
    queryset = Option.objects.all()
    success_url = '/app/Creationoption'
    messages = ""
    
    def post(self, request, *args, **kwargs):
        form = OptionCreateForm(request.POST)
        if form.is_valid():
           form.save()
           form = OptionCreateForm()
           self.messages = "Opération réussie"
        else:
            self.messages = "Opération non réuissie"
        return render(request, self.template_name, {'messages': self.messages, "form": form})    

#####-------Création épreuve-----------
class EpreuveCreate(LoginRequiredMixin,CreateView): 
    template_name = 'create-epreuve.html'
    form_class = EpreuveCreateForm
    queryset = Epreuve.objects.all()
    success_url = '/app/epreuvecreate'
    messages = ""
    
    def post(self, request, *args, **kwargs):
        form = EpreuveCreateForm(request.POST)
        if form.is_valid():
           form.save()
           form = EpreuveCreateForm()
           self.messages = "Opération réussie"
        else:
            self.messages = "Opération non réuissie"
        return render(request, self.template_name, {'messages': self.messages, "form": form})    
    
#####-------Création cours-----------
class CoursCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView): 
    permission_required ='Cours.can_add'
    template_name = 'create-cours.html'
    form_class = CoursCreateForm
    queryset = Cours.objects.all()
    success_url = '/app/courscreate'
    messages = ""
    
    def post(self, request, *args, **kwargs):
        form = CoursCreateForm(request.POST)
        if form.is_valid():
           form.save()
           form = CoursCreateForm()
           self.messages = "Opération réussie"
        else:
            self.messages = "Opération non réuissie"
        return render(request, self.template_name, {'messages': self.messages, "form": form})

    
    
#####-------Création passer-----------
class PasseCreate(LoginRequiredMixin,CreateView):
    template_name = 'create-passe.html'
    form_class = PasserCreateForm
    queryset = Passer.objects.all()
    success_url = '/app/passecreate'
    
    def post(self, request, *args, **kwargs):
        form = PasserCreateForm(request.POST)
        if form.is_valid():
           form.save()
           form = PasserCreateForm()
           self.messages = "Opération réussie"
        else:
            self.messages = "Opération non réuissie"
        return render(request, self.template_name, {'messages': self.messages, "form": form})

#-------------EDITION--------------
@user_passes_test(Is_Administration)
def Edition(request):
    return render(request,'edition.html')

#---------------------PROCLAMATION---------------------
def SommePartielle(value,*args, **kwargs):
    pass

def Palmares(request): 
    
    try:
        pass
    except Passer.DoesNotExist:
           raise Http404
    context = {
        
    }
    return render(request, 'proclamation.html', context)