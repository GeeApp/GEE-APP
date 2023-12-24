from django.db import models

# Create your models here.
class Classe(models.Model):
    code_class = models.CharField("Code-Classe", max_length=50, blank=False)
    lib_class = models.CharField("Libellé-Classe", max_length=20, null=False)
    
    
    class Meta():
        verbose_name = ('Classe')
        verbose_name_plural = ('Classes')
        
    def __str__(self) -> str:
        return self.lib_class

class Option(models.Model):
    code_opt = models.CharField("Code-Option", max_length=50, blank=False)
    lib_opt = models.CharField("Libellé-Option", max_length=20, null=False)
    
    def __str__(self) -> str:
        return self.lib_opt
    
class Eleve(models.Model):
    matr_eleve = models.CharField("Matricule", blank=False,max_length=30)
    nom_el = models.CharField("Nom-Elève", max_length=30, null=False)
    post_nom_el = models.CharField("Post-Nom-Elève", max_length=30, null=False,default="")
    prenom_el = models.CharField("Prenom-Elève", max_length=30, null=False,default="")
    date_nais_el = models.CharField("Date-naissance-Elève", max_length=30, null=False,default="")
    sexe_el = models.CharField("Sexe Elève", max_length=1, null=False, default="M")
    nom_titeur = models.CharField("Nom-Titeur", max_length=30, null=False,default="")
    classe = models.ForeignKey(Classe,  on_delete=models.CASCADE, default=1)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, default=1)
    Adress_el = models.CharField("Adresse-Elève", max_length=30, default="")
    Tel_titeur = models.CharField("Numéro-tuteur", max_length=30, null=False,default="")
    
    def __str__(self) -> str:
        return self.nom_el
    
class Enseigant(models.Model):
    nom_ens =  models.CharField("Nom-Enseignant", max_length=30, null=False)
    matr_ens = models.CharField("Matricule-Enseignant", blank=False,max_length=30)
    post_ens = models.CharField("Post-Nom-Enseigant", max_length=30, null=False,default="")
    prenom_ens = models.CharField("Prenom-Enseigant", max_length=30, null=False,default="")
    date_nais_ens = models.CharField("Date-Naissance-Enseigant", max_length=30, null=False,default="")
    sexe_ens = models.CharField("Sexe", max_length=1, null=False, default="M")
    etat_civil_ens = models.CharField("Etat-Civil", max_length=1, null=False, default="C")
    niveau_etude =models.CharField("Niveau-D'étude",max_length=30, null=False)
    adresse_ens = models.CharField("Adresse-Enseignant", max_length=30, default="")
    date_engagement = models.CharField("Date-Engagement", max_length=30, null=False,default="")
    tel_ens = models.CharField("Numéro-Enseigant", max_length=30, null=False,default="")
    
    
    def __str__(self) -> str:
        return self.nom_ens
    
class Cours(models.Model):
    code_cours =  models.CharField("Code-Cours", blank=False,max_length=30)
    lib_cours =  models.CharField("Nom-Cours", blank=False,max_length=100)
    Ponderation = models.IntegerField("Pondération", blank=False)
    
    class Meta:
        verbose_name = ("Cours")
        verbose_name_plural = ("Cours")
    
    
    def __str__(self) -> str:
        return self.lib_cours
    
class Epreuve(models.Model):
    code_epr = models.CharField("Code-Epreuve", blank=False, max_length=4)
    Lib_epr = models.CharField("Libéllé-Epreuve", blank=False,max_length=40)
    max_epr = models.CharField("Max-Epreuve",blank=True,max_length=3)
    
     
    def __str__(self) -> str:
        return self.Lib_epr

class Appartenir(models.Model):
    anne_scol = models.CharField("Anne-Scolaire", max_length=30, null=False)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    
     
    def __str__(self) -> str:
        return self.eleve.nom_el

class Periode(models.Model):
    code_per = models.CharField("Code-Période", blank=False,max_length=30)
    lib_periode = models.CharField("Libéllé-Période", blank=False,max_length=50)
    
    
    def __str__(self) -> str:
        return self.lib_periode

class Semestre(models.Model):
    code_sem = models.CharField("Code-Semestre", blank=False,max_length=30)
    lib_sem = models.CharField("Libéllé-Semestre", blank=False,max_length=50)
    
    
    def __str__(self) -> str:
        return self.lib_sem
    
class Passer(models.Model):
    eleve_pas = models.ForeignKey(Eleve, on_delete=models.CASCADE,verbose_name="Eleve")
    epreuve_pas = models.ForeignKey(Epreuve, on_delete=models.CASCADE,verbose_name="Epreuve")
    cours_pas = models.ForeignKey(Cours, on_delete=models.CASCADE,verbose_name="Cours")
    date_pass = models.CharField("Date", max_length=30, blank=False)
    point_obt =models.IntegerField("Point-Obtenu",  blank=False)
   #max_cours = models.IntegerField("Maximum-Epreuve", blank=False)
    periode =  models.ForeignKey(Periode, on_delete=models.CASCADE,verbose_name="Période")
    semestre =  models.ForeignKey(Semestre, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.eleve_pas.nom_el
    
class Dispenser(models.Model):
    classe_disp = models.ForeignKey(Classe, on_delete=models.CASCADE)
    cours_disp = models.ForeignKey(Cours, on_delete=models.CASCADE)
    enseigant_disp = models.ForeignKey(Enseigant, on_delete=models.CASCADE)
    anne_scol_disp =  models.CharField("Année-Scolaire", max_length=30, blank=False)
    
    def __str__(self) -> str:
        return self.classe_disp.lib_class

class Titulaire(models.Model):
    enseigant_titulaire = models.ForeignKey(Enseigant, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    anne_scol =  models.CharField("Année-Scolaire", max_length=30, blank=False)
    
    def __str__(self) -> str:
        return self.enseigant_titulaire.nom_ens
