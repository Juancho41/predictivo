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

class Componente(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.nombre, self.equipo)

class PuntoMedicion(models.Model):
    punto = models.CharField(max_length=1)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)

    def __str__(self):
        return "Punto {} del componente {}".format(self.punto, self.componente)



class Medicion(models.Model):
    punto = models.ForeignKey(PuntoMedicion, on_delete=models.CASCADE)
    val_vibracion = models.IntegerField(null=TRUE, blank=TRUE)
    val_ultSonido = models.IntegerField(null=TRUE, blank=TRUE)
    fechaMedicion = models.DateTimeField()
    fechaRegistro = models.DateTimeField(auto_now=TRUE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=TRUE)

    def __str__(self):
        return "{} - {}".format(self.punto, self.fechaMedicion)
