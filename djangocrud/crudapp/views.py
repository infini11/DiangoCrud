from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Tache

# Create your views here.

def home(request):
	return render(request, "home.html")

def listetache(request):
	return render(request, "listetache.html")


def enregistrer(request):
	form = TacheForm(data=request.POST)
	if (request.method == "POST"):
		if form.is_valid():
			nomtache = form.data['nomtache']
			description = form.data['description']
			debut =  form.data['debut']
			fin = form.data['fin']
			print(nomtache, description, debut, fin)

			tache = Tache(nomtache=nomtache, description=description, debut=debut, fin=fin) 
			tache.save()

			return render(request, "listetache.html")

	context = {"form" : form}

	return render(request, "formulaire.html", context)