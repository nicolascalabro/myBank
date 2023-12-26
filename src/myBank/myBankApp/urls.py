from django.urls import path
from myBankApp.views import index, clientes, cuentas, nomina 

urlpatterns = [
    path("", index, name = "index"),
    path("clientes/", clientes, name = "clientes"), 
    path("cuentas/", cuentas, name = "cuentas"),
    path("nomina/", nomina, name = "nomina"),
]