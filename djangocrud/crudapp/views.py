from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import Tache

# Create your views here.

def home(request):
	return render(request, "home.html")


def listeTache(request):
	queryset = Tache.objects.all()
	context = {
		"object_tache": queryset
	}

	return render(request, "listetache.html", context)  


def enregistrerTache(request):
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

			queryset = Tache.objects.all()
			context = {
				"object_tache": queryset
			}
			return render(request, "listetache.html", context)

	context = {"form" : form}

	return render(request, "formulaire.html", context)


def updateTache(request, id):
	instance = Tache.objects.get(id=id)
	form =TacheForm(data=request.POST, instance=instance)
	if form.is_valid():
		form.save()
		return render(request, "formulaire.html")

	context = {"form": form}
	return render(request, "update.html", context)


def deleteTache(request, id):
	instance = Tache.objects.get(id=id)
	instance.delete()
	return redirect ("delete.html")

