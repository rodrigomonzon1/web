from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User
from .models import Usuario, InfoUsuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'edad']


class RegistroDeUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {
            key: ''
            for key in fields
        }


class EditarPerfil(forms.ModelForm):
    email = forms.EmailField(required=False)  # Campo de User
    avatar = forms.ImageField(required=False)  # Campo de InfoUsuario

    class Meta:
        model = User
        fields = ['email']  # Solo los campos del modelo User

    def __init__(self, *args, **kwargs):
        # Acepta la instancia de InfoUsuario como un argumento adicional
        self.info_usuario_instance = kwargs.pop('info_usuario_instance', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=commit)
        if self.info_usuario_instance:
            avatar = self.cleaned_data.get('avatar')
            if avatar:
                self.info_usuario_instance.avatar = avatar
                if commit:
                    self.info_usuario_instance.save()
        return user
