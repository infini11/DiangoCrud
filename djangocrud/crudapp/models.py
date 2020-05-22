from django.db import models

# Create your models here.

class Tache(models.Model):
	nomtache = models.CharField(max_length=200)
	description = models.TextField()
	debut = models.DateField(blank=True)
	fin = models.DateField(blank=True)