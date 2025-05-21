from django.db import models

# Create your models here.
class Bebida(models.Model):
    idbebida=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion=models.CharField(max_length=250)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=1500)
    
    def __str__(self):
        return self.nombre
    
class Menu(models.Model):
    idMenu=models.AutoField(primary_key=True)
    nombreMenu = models.CharField(max_length=50)
    detalleMenu=models.CharField(max_length=250)
    precioMenu = models.IntegerField()
    imagenMenu = models.CharField(max_length=1500)
    
    def __str__(self):
        return self.nombreMenu
    

class AlmuerzoEjecu(models.Model):
    sopas = models.CharField(max_length=150)
    principio = models.CharField(max_length=150)
    carnes = models.CharField(max_length=250)
    bebida = models.CharField(max_length=150)
    imagenSopa = models.CharField(max_length=800, null=True)
    imagenBandeja = models.CharField(max_length=800, null=True)
    
    def __str__(self):
        return self.sopas