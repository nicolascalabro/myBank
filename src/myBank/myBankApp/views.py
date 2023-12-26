from django.shortcuts import render
from myBankApp.models import Cliente, Cuenta, Nomina
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def clientes(request):
    if request.method == "POST":
        nombre_cliente = request.POST.get("nombre_cliente")
        apellido_cliente = request.POST.get("apellido_cliente")
        dni_cliente = request.POST.get("dni_cliente")
        email_cliente = request.POST.get("email_cliente")
       
        cliente = Cliente(nombre=nombre_cliente, apellido=apellido_cliente, dni=dni_cliente, email=email_cliente)
        cliente.save()

    return render(request, "clientes.html")

def cuentas(request):
    if request.method == "POST":
        titular_cuenta = request.POST.get("titular_cuenta")
        numero_cuenta = request.POST.get("numero_cuenta")
        fecha_cuenta = request.POST.get("fecha_cuenta")
        estado_cuenta = request.POST.get("estado_cuenta") == "on"  #En HTML, el checkbox actuivado es enviado como "on" en el formulario. 
        saldo_cuenta = request.POST.get("saldo_cuenta")
              
        cuenta = Cuenta(titular=titular_cuenta, numero=numero_cuenta, fechaCreacion=fecha_cuenta, estado=estado_cuenta, saldo=saldo_cuenta)
        cuenta.save()

    return render(request, "cuentas.html")

def nomina(request):
    if request.method == "POST":
        nombre_empleado = request.POST.get("nombre_empleado")
        apellido_empleado = request.POST.get("apellido_empleado")
        puesto_empleado = request.POST.get("puesto_empleado")
      
        empleado = Nomina(nombre=nombre_empleado, apellido=apellido_empleado, puesto=puesto_empleado)
        empleado.save()
    return render(request, "nomina.html")

def buscar_cuenta(request):
    cuenta = []
    if "numero_cuenta" in request.GET:
        numero = request.GET.get("numero_cuenta")
        cuenta = Cuenta.objects.filter(numero__icontains = numero)   
    return render(request, "buscar_cuenta.html", {"cuenta": cuenta})      