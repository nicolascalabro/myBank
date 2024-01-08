from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ["apellido"]

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"
    
class Cuenta(models.Model):
    titular = models.CharField(max_length=40)
    numero = models.IntegerField()
    fechaCreacion = models.DateField()
    estado = models.BooleanField(default=True)
    saldo = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cuentas"
        ordering = ["numero"]

    def __str__(self):
        return f"Nro de cuenta: {self.numero} - Titular: {self.titular} - Estado: {self.estado}"    

class Nomina(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    puesto = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Nomina"
        ordering = ["apellido"]

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Puesto: {self.puesto}"