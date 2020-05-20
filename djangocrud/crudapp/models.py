from django.db import models

# Create your models here.

class tache(models.Model):
	nomtache = models.CharField(max_length=200)
	description = models.TextField()
	debut = models.DateField()
	fin = models.DateField()