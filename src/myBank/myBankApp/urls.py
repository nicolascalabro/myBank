from django.urls import path
from myBankApp.views import index, clientes, cuentas, nomina, buscar_cuenta

urlpatterns = [
    path("", index, name = "index"),
    path("clientes/", clientes, name = "clientes"), 
    path("cuentas/", cuentas, name = "cuentas"),
    path("nomina/", nomina, name = "nomina"),
    path("buscar/", buscar_cuenta, name = "buscar_cuenta"),
]