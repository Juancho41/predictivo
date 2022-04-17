from enum import auto
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MiniPlanta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre



class Sector(models.Model):
    miniPlanta = models.ForeignKey(MiniPlanta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    creacion = models.DateTimeField(auto_now=TRUE)

    def __str__(self):
        return self.nombre


class Medicion(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    val_vibracion = models.IntegerField(null=TRUE, blank=TRUE)
    val_ultSonido = models.IntegerField(null=TRUE, blank=TRUE)
    fechaMedicion = models.DateTimeField(auto_now=TRUE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=TRUE)

    def __str__(self):
        return "{} - {}".format(self.equipo, self.fechaMedicion)
