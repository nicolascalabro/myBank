from django.urls import path
from myBankApp.views import (
    index, 
    clientes,
    cuentas, 
    nomina, 
    buscar_cuenta, 
    listar_clientes, 
    eliminar_cliente, 
 )

urlpatterns = [
    path("", index, name = "index"),
    path("clientes/", clientes, name = "clientes"), 
    path("cuentas/", cuentas, name = "cuentas"),
    path("nomina/", nomina, name = "nomina"),
    path("buscar/", buscar_cuenta, name = "buscar_cuenta"),
    path("listar_clientes/", listar_clientes, name = "listar_clientes"),
    path("eliminar_cliente/<cliente_apellido>", eliminar_cliente, name = "eliminar_cliente"),
]