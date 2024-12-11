from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'activo']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }
