# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Farmacia(models.Model):
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=200, null=False, blank=False, unique=True)
    reputacion = models.CharField(max_length=30, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)    
    latitud = models.CharField(max_length=50, null=True, blank=True)
    longitud = models.CharField(max_length=50, null=True, blank=True)
    horario_atencion = models.CharField(max_length=100, null=True, blank=True)
    
class ComentarioFarmacia(models.Model):
    estado = models.BooleanField(default=True)
    farmacia  = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    observacion = models.TextField(max_length=1000, null=False, blank=False)
    calificacion = models.IntegerField(null=True, blank=True)

class Tnovedad(models.Model):
    estado = models.BooleanField(default=True)
    nombre = models.CharField(max_length=200, null=False, blank=False, unique=True) 
    
class Novedad(models.Model):
    estado = models.BooleanField(default=True)
    farmacia  = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    tnovedad  = models.ForeignKey(Tnovedad, on_delete=models.CASCADE)
    registro_invima = models.CharField(max_length=50, null=False, blank=False)
    expediente = models.TextField(max_length=1000, null=False, blank=False)
    consecutivo = models.CharField(max_length=50, null=True, blank=True)
    observacion = models.TextField(max_length=1000, null=False, blank=False)
    