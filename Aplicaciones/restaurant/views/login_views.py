from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Usuario'},
    ), label='Usuario')
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
        label='Contraseña',
    )