from django.db import models

class auto(models.Model):
    marca = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 30)
    modelo = models.IntegerField()
    color = models.CharField(max_length =20)
    def __str__(self):
        return 'marca: %s, nombre: %s, modelo: %s, color: %s,' %(self.marca, self.nombre, self.modelo, self.color)

class cliente(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 200)
    email = models.CharField(max_length=250)
    telefono = models.CharField(max_length = 20)
    def __str__(self):
        return 'nombre: %s, apellido: %s, direccion: %s, email: %s, telefono:%s' %(self.nombre, self.apellido, self.direccion, self.email, self.telefono)