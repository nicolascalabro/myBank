from django.urls import path
from django.contrib.auth.views import LogoutView

from myBankApp.views import (
    index, 
    clientes,
    cuentas, 
    nomina, 
    buscar_cuenta, 
    listar_clientes, 
    eliminar_cliente,
    editar_cliente,
    login_request,
    registrar,
    editar_usuario,
    panel_admin,
    acerca_de,    
 )

urlpatterns = [
    path("", index, name = "index"),
    path("clientes/", clientes, name = "clientes"), 
    path("cuentas/", cuentas, name = "cuentas"),
    path("nomina/", nomina, name = "nomina"),
    path("buscar/", buscar_cuenta, name = "buscar_cuenta"),
    path("listar_clientes/", listar_clientes, name = "listar_clientes"),
    path("eliminar_cliente/<cliente_apellido>", eliminar_cliente, name = "eliminar_cliente"),
    path("editar_cliente/<cliente_apellido>", editar_cliente, name = "editar_cliente"),
    path("login/", login_request, name = "login"),
    path("registrar/", registrar, name = "registrar"),
    path("logout/", LogoutView.as_view(template_name = "index.html"), name = "logout"),
    path("editar_usuario/", editar_usuario, name = "editar_usuario"),
    path("panel_admin/", panel_admin, name = "panel_admin"),
    path("acerca_de/", acerca_de, name = "acerca_de"),
]