from django.contrib import admin
from django.urls import path
from . import views


app_name = "crudapp"


urlpatterns = [
    path('', views.home),
    path('enregistrer/', views.enregistrer, name="enregistrer"),
    path('afficher/', views.listetache),
]
