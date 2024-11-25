from django.db import models

class Admins(models.Model):
    id = models.CharField(primary_key=True,max_length=16)
    nom = models.CharField(max_length=20)  
    prenom = models.CharField(max_length=70,blank=False)
    password = models.CharField(max_length=12,blank=False)
    birthdate = models.DateTimeField(blank=False)  
    date_creation = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.champ1
    
class Matiere(models.Model):
    name = models.CharField(max_length=100)  
    code = models.CharField(max_length=10, unique=True)  

    def __str__(self):
        return self.name
    
class Classe(models.Model):
    name = models.CharField(max_length=50)  # Nom de la classe
    year = models.IntegerField()  # Année scolaire ou niveau (exemple : 6, 5, Terminale)
 
    def __str__(self):
        return self.name
    
class Professeur(models.Model):
    id = models.CharField(primary_key=True,max_length=16)
    nom = models.CharField(max_length=20)  
    prenom = models.CharField(max_length=70,blank=False)
    password = models.CharField(max_length=12,blank=False)
    birthdate = models.DateTimeField(blank=False)  
    matiere = models.ForeignKey(Matiere)
    classes = models.ManyToManyField(Classe, related_name="professeur")

    def __str__(self):
        return f"{self.nom, self.prenom} - {self.matiere.name}"


class Etudiant(models.Model):
        id = models.CharField(primary_key=True,max_length=16)
        nom = models.CharField(max_length=20)  
        prenom = models.CharField(max_length=70,blank=False)
        password = models.CharField(max_length=12,blank=False)
        birthdate = models.DateTimeField(blank=False)  
        classe = models.ForeignKey(Classe, related_name="etudiant")
    def __str__(self):
        return f"{self.nom , self.prenom} - {self.classe.name}"

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="notes")  
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="notes")  
    note = models.DecimalField(max_digits=5, decimal_places=2)  

    class Meta:
        unique_together = ('etudiant', 'matiere')  

    def __str__(self):
        return f"{self.etudiant.nom ,self.etudiant.prenom } - {self.matiere.name}: {self.note}"
