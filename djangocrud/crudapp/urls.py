from django.contrib import admin
from django.urls import path
from . import views


app_name = "crudapp"


urlpatterns = [
    path('', views.home),
    path('enregistrer/', views.enregistrerTache, name="enregistrer"),
    path('listetache/', views.listeTache),
    path('update/', views.updateTache, name="update"),
    path('delete/', views.deleteTache, name="delete"),
]
