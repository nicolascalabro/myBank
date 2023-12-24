from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ["apellido"]

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido}"
    
class Cuenta(models.Model):
    titular = models.CharField(max_length=50)
    numero = models.IntegerField()
    fechaCreacion = models.DateField()
    estado = models.BooleanField()
    saldo = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cuentas"
        ordering = ["numero"]

    def __str__(self):
        return f"Nro de cuenta: {self.numero} - Titular: {self.titular} - Estado: {self.estado}"    

class Sucursal(models.Model):
    numero = models.IntegerField()
    direccion = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = "Sucursales"
        ordering = ["numero"]

    def __str__(self):
        return f"Numero de sucursal: {self.numero} - Direccion: {self.direccion}"