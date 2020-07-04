from django.contrib import admin
from django.urls import path
from . import views


app_name = "crudapp"


urlpatterns = [
    path('', views.home, name='home'),
    path('enregistrer/', views.enregistrerTache, name="enregistrer"),
    path('ListeTache/', views.listeTache, name="listeTache"),
    path('update/', views.updateTache, name="update"),
    path('delete/', views.deleteTache, name="delete"),
    path('delete/', views.deleteTache, name="delete"),

]
