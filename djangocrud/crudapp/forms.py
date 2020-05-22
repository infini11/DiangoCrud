from django import forms
from .models import *


class TacheForm(forms.ModelForm):
	class Meta:
		model = Tache
		fields = ['nomtache', 'description', 'debut', 'fin']