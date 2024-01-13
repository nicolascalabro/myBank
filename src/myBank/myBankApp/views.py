from django.shortcuts import render
from myBankApp.models import Cliente, Cuenta, Nomina
from django.http import HttpResponse

from myBankApp.forms import ClienteFormulario, CuentaFormulario, NominaFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "index.html")

def clientes(request):

    if request.method == "POST":
        clienteFormulario = ClienteFormulario(request.POST)
        if clienteFormulario.is_valid():
            data = clienteFormulario.cleaned_data

            nombre_cliente = data.get("nombre")
            apellido_cliente = data.get("apellido")
            dni_cliente = data.get("dni")
            email_cliente = data.get("email")

            cliente = Cliente(nombre=nombre_cliente, apellido=apellido_cliente, dni=dni_cliente, email=email_cliente)
            cliente.save()
            return render(request, "index.html")
    else:
        clienteFormulario = ClienteFormulario() 
    return render(request, "clientes.html", {"clienteFormulario": clienteFormulario})

def cuentas(request):
    if request.method == "POST":
        cuentaFormulario = CuentaFormulario(request.POST)
        if cuentaFormulario.is_valid():
            data = cuentaFormulario.cleaned_data

            titular_cuenta  = data.get("titular")
            numero_cuenta  = data.get("numero")
            fecha_cuenta  = data.get("fechaCreacion")
            estado_cuenta  = data.get("estado")
            saldo_cuenta  = data.get("saldo")
           
            cuenta = Cuenta(titular=titular_cuenta, numero=numero_cuenta, fechaCreacion=fecha_cuenta, estado=estado_cuenta, saldo=saldo_cuenta)
            cuenta.save()
            return render(request, "index.html")       
    else:
        cuentaFormulario = CuentaFormulario()
    return render(request, "cuentas.html", {"cuentaFormulario": cuentaFormulario})

def nomina(request):
    if request.method == "POST":
        nominaFormulario = NominaFormulario(request.POST)
        if nominaFormulario.is_valid():
            data = nominaFormulario.cleaned_data

            nombre_empleado = data.get("nombre")
            apellido_empleado = data.get("apellido")
            puesto_empleado = data.get("puesto")
            
            empleado = Nomina(nombre=nombre_empleado, apellido=apellido_empleado, puesto=puesto_empleado)
            empleado.save()
            return render(request, "index.html")
    else:
        nominaFormulario = NominaFormulario()    
    return render(request, "nomina.html", {"nominaFormulario": nominaFormulario})

def buscar_cuenta(request):
    cuenta = []
    if "numero_cuenta" in request.GET:
        numero = request.GET.get("numero_cuenta")
        cuenta = Cuenta.objects.filter(numero__icontains = numero)   
    return render(request, "buscar_cuenta.html", {"cuenta": cuenta})      


def listar_clientes(request):
    clientes = Cliente.objects.all()
    print(clientes)
    contexto = {
        "key_clientes": clientes,
    }
    return render(request, "listar_clientes.html", contexto)

def eliminar_cliente(request, cliente_apellido):
    cliente = Cliente.objects.get(apellido = cliente_apellido)
    cliente.delete()

    clientes = Cliente.objects.all()
    contexto = {
        "key_clientes": clientes,
    }
    return render(request, "listar_clientes.html", contexto) 