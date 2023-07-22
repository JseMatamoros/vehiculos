from django.db import models
from django.contrib.auth.models import AbstractUser


class Vehiculo(models.Model):
    MARCAS = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    CATEGORIAS = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    CONDICIONES_PRECIO = (
        ('Bajo', 'Bajo'),
        ('Medio', 'Medio'),
        ('Alto', 'Alto'),
    )

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=8, decimal_places=2)    
    condicion_precio = models.CharField(max_length=10, blank=True)
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)  # Agregar campo de imagen

    def save(self, *args, **kwargs):
        if self.precio < 10000:
            self.condicion_precio = 'Bajo'
        elif self.precio < 30000:
            self.condicion_precio = 'Medio'
        else:
            self.condicion_precio = 'Alto'
        super().save(*args, **kwargs)
        
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marca + ' ' + self.modelo
