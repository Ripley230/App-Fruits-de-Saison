from django.db import models

class Saison(models.Model):
    nom = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.nom

class Fruit(models.Model):
    nom = models.CharField(max_length=100)
    saison = models.ForeignKey(Saison, on_delete=models.CASCADE, related_name='fruits')

    def __str__(self):
        return self.nom