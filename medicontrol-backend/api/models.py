# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Farmacia(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    reputacion = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    
class ComentarioFarmacia(models.Model):
    farmacia  = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    observacion = models.TextField(max_length=1000, null=False, blank=False)
    calificacion = models.CharField(max_length=50, null=True, blank=True)
    