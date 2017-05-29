from django import forms
from webpage.models import *

class WebpageForm(forms.ModelForm):
	class Meta:
		model = FormularioContacto