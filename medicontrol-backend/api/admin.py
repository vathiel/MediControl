# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Farmacia, ComentarioFarmacia, Tnovedad, Novedad
from django.contrib import admin

# Register your models here.

class FarmaciaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_display =  ['nombre', 'reputacion', 'direccion', 'telefono', 'latitud', 'longitud', 'horario_atencion','estado']

class FarmaciaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_display =  ['nombre', 'reputacion', 'direccion', 'telefono', 'latitud', 'longitud', 'horario_atencion','estado']



admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(ComentarioFarmacia)
admin.site.register(Tnovedad)
admin.site.register(Novedad)