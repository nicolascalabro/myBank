from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    email = forms.EmailField()

class CuentaFormulario(forms.Form):
    titular = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    fechaCreacion = forms.DateField()
    estado = forms.BooleanField()
    saldo = forms.IntegerField()    

class NominaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    puesto = forms.CharField(max_length=30)   