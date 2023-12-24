from django.urls import path
from myBankApp.views import index, clientes, cuentas, sucursales 

urlpatterns = [
    path("", index, name = "index"),
    path("clientes/", clientes, name = "clientes"), 
    path("cuentas/", cuentas, name = "cuentas"),
    path("sucursales/", sucursales, name = "sucursales"),
]