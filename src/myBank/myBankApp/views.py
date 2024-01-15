from django.shortcuts import render
from myBankApp.models import Cliente, Cuenta, Nomina
from django.http import HttpResponse

from myBankApp.forms import ClienteFormulario, CuentaFormulario, NominaFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

@login_required
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

#-------------------CRUD-------------------
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "listar_clientes.html", {"clientes": clientes})

def eliminar_cliente(request, cliente_apellido):
    cliente = Cliente.objects.get(apellido = cliente_apellido)
    cliente.delete()

    clientes = Cliente.objects.all()
    return render(request, "listar_clientes.html", {"clientes": clientes})

def editar_cliente(request, cliente_apellido):
    cliente = Cliente.objects.get(apellido = cliente_apellido)

    if request.method == "POST":
        clienteFormulario = ClienteFormulario(request.POST)
        if clienteFormulario.is_valid():
            data = clienteFormulario.cleaned_data

            cliente.nombre = data.get("nombre")
            cliente.apellido = data.get("apellido")
            cliente.dni = data.get("dni")
            cliente.email = data.get("email")

            cliente.save()
            return render(request, "index.html")

    clienteFormulario = ClienteFormulario(initial = {
        "nombre": cliente.nombre, 
        "apellido": cliente.apellido,
        "dni": cliente.dni,
        "email": cliente.email
        }) 
    return render(request, "editar_cliente.html", {"clienteFormulario": clienteFormulario, "cliente_apellido": cliente.apellido})

#-------------------Manejo de usuarios-------------------
def login_request(request):
    if request.method == "POST":
        authenticationForm = AuthenticationForm(request, data = request.POST)
        if authenticationForm.is_valid():
            data = authenticationForm.cleaned_data

            usuario = data.get("username")
            contraseña = data.get("password")
        
            user = authenticate(username = usuario, password = contraseña)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "index.html", {"mensaje": f"Usuario o contraseña invalidos"})
        else:
            return render(request, "index.html", {"mensaje": "Datos incorrectos"})    
    else:
        authenticationForm = AuthenticationForm() 
    return render(request, "login.html", {"authenticationForm": authenticationForm})

def registrar(request):
    if request.method == "POST":
        userCreationForm = UserCreationForm(request.POST)
        if userCreationForm.is_valid():
            data = userCreationForm.cleaned_data

            usuario = data.get("username")

            userCreationForm.save()
            return render(request, "index.html", {"mensaje": f"Se ha creado el usuario {usuario}"})
    else:
        userCreationForm = UserCreationForm() 
    return render(request, "registrar.html", {"userCreationForm": userCreationForm})