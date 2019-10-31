from django import forms
from .models import Usuario

class Usuarioform(forms.ModelForm):
    passw = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = Usuario
        fields = ['id_cliente', 'nombre', 'apellidos', 'edad', 'email', 'passw',]