from django.db import models
from django.core.validators import MaxValueValidator


class ModeloInventario(models.Model):

    Unidades = [
        ('PI', 'PI'),
        ('GLN', 'GLN'),
        ('CJ', 'CJ'),
        ('CUB', 'CUB'),
        ('TR', 'TR'),
        ('KG', 'KG'),
        ('KIT', 'KIT'),
        ('L', 'L'),
        ('M', 'M'),
        ('PAA', 'PAA'),
        ('ROL', 'ROL'),
        ('T', 'T'),
        ('TOT', 'TOT'),
    ]

    Valoracion = [
        ('FABRICADO', 'FABRICADO'),
        ('REPARADO', 'REPARADO'),
        ('LINEA CONS', 'LINEA CONS'),
        ('LINEA PROP', 'LINEA PROP'),
        ('RECUPERADO', 'RECUPERADO'),
        ('INV CAP', 'INV CAP'),
        ('DAÑADO', 'DAÑADO'),
        ('CAP SPARE', 'CAP SPARE'),
        ('CALIBRADO', 'CALIBRADO'),
    ]

    Almacenes = [
        ('Santa Catarina', 1001),
        ('Garcia', 1002),
        ('Aerospace', 1003),
        ('Forja Abierta', 1004),
        ('Aceria', 1005),
        ('Precision', 1006),
    ]

    codigo           = models.IntegerField(validators=[MaxValueValidator(9999999)])
    cantidad         = models.IntegerField()
    unidad_medida    = models.CharField(max_length=20, choices=Unidades, default=None)
    clase_valoracion = models.CharField(max_length=20, choices=Valoracion, default=None)
    descripcion      = models.CharField(max_length=40)
    ubicacion        = models.CharField(max_length=13)
    almacen          = models.CharField(max_length=20, choices=Almacenes, default=None)
    modelo           = models.CharField(max_length=50, default=None)
    marca            = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.descripcion
