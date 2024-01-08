from django.urls import path
from myBankApp.views import index, clientes, cuentas, nomina, buscar_cuenta, leer_clientes, eliminar_cliente

urlpatterns = [
    path("", index, name = "index"),
    path("clientes/", clientes, name = "clientes"), 
    path("cuentas/", cuentas, name = "cuentas"),
    path("nomina/", nomina, name = "nomina"),
    path("buscar/", buscar_cuenta, name = "buscar_cuenta"),
    path("leer_clientes/", leer_clientes, name = "leer_clientes"),
    path("eliminar_cliente/<nombre_cliente>", eliminar_cliente, name = "eliminar_cliente"),
]