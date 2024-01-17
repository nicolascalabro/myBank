from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    email = forms.EmailField()

class CuentaFormulario(forms.Form):
    titular = forms.CharField(max_length=40)
    numero = forms.IntegerField(label="Numero de Cuenta")
    fechaCreacion = forms.DateField(label="Fecha de Creacion")
    estado = forms.BooleanField()
    saldo = forms.IntegerField()    

class NominaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    puesto = forms.CharField(max_length=30)   

class UserRegFormulario(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()  
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]   

class UserEditFormulario(UserCreationForm):
    email = forms.EmailField()  
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) 
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name"]