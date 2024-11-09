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