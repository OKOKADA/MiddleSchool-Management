from django.db import models

class Admins(models.Model):
    id = models.CharField(primary_key=True,max_length=16)
    nom = models.CharField(max_length=20)  
    prenom = models.CharField(max_length=70,blank=False)
    password = models.CharField(max_length=12,blank=False)
    birthdate = models.DateTimeField(blank=False)  
    date_creation = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.id
    
from django.db import models

#Classe Enseignants

class Teachers(models.Model):
    # Attributs de la classe Teachers
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    annee_prise_fonction = models.IntegerField(blank=False)
    specialite = models.CharField(max_length=100, blank=False)
    cours_dispenses = models.TextField(blank=True)  # Liste des cours sous forme de texte, ou relation ManyToMany avec un modèle Cours

    # Méthodes

    def consulter_planning(self):
        """
        Simule la consultation du planning de l'enseignant.
        Retourne un message générique ou interagit avec un modèle de Planning.
        """
        return f"Planning consulté pour {self.nom} {self.prenom}."

    def attribuer_note(self, etudiant, cours, note):
        """
        Simule l'attribution d'une note à un étudiant pour un cours donné.
        """
        # Ici, tu pourrais lier cette méthode à un modèle Notes qui stocke les notes des étudiants
        return f"Note {note} attribuée à {etudiant} pour le cours {cours}."

    def televerser_cours(self, cours, fichier):
        """
        Simule le téléversement d'un fichier de cours.
        """
        # Cette méthode pourrait être liée à un système de gestion de fichiers
        return f"Le fichier '{fichier}' a été téléversé pour le cours '{cours}'."

    def consulter_notes(self, etudiant, cours):
        """
        Simule la consultation des notes d'un étudiant pour un cours donné.
        """
        return f"Consultation des notes pour {etudiant} dans le cours {cours}."

    def generer_releve_notes(self, etudiant):
        """
        Simule la génération d'un relevé de notes pour un étudiant.
        """
        return f"Relevé de notes généré pour l'étudiant {etudiant}."

    def __str__(self):
        return f'{self.nom} {self.prenom} - Spécialité : {self.specialite}'