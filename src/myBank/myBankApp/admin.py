from django.contrib import admin

from myBankApp.models import Cliente, Cuenta, Nomina

admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Nomina)