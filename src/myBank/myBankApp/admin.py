from django.contrib import admin

from myBankApp.models import Cliente, Cuenta, Sucursal

admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Sucursal)