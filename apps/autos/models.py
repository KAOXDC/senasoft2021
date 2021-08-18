from django.db import models

# Create your models here.
colores = (
    ('rojo','rojo'),
    ('azul','azul'),
    ('plata','plata'),
    ('negro','negro'),
)


# Clase Marca para el vehiculo
class Marca (models.Model):
    nombre      = models.CharField(max_length = 50)

    def __str__ (self):
        return self.nombre


class Auto (models.Model):
    pasajeros   = models.CharField(max_length = 3)
    cilindraje  = models.IntegerField(blank= True, null=True)
    color       = models.CharField(max_length=50, choices = colores)
    puertas     = models.PositiveIntegerField()
    foto        = models.ImageField(upload_to = 'autos', blank=True, null =True) # las imagenes se guardan en media/autos
    marca       = models.ForeignKey(Marca, on_delete=models.PROTECT)

    def __str__ (self):
        return self.color + " " + str(self.cilindraje) + ' ' + self.marca.nombre

