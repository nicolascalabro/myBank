from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def cuentas(request):
    return render(request, "cuentas.html")

def clientes(request):
    return render(request, "clientes.html")

def sucursales(request):
    return render(request, "sucursales.html")