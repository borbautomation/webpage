from django import forms
from webpage.models import *

class WebpageForm(forms.ModelForm):
	class Meta:
		model = FormularioContacto
		fields = ['nombre','compania','email','text']
		widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'compania': forms.TextInput(attrs={'placeholder': 'Compañia'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            
            'text': forms.Textarea(
                attrs={'placeholder': 'Mandanos tu mensaje...'}),
        }