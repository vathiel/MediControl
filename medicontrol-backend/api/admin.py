# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Farmacia, ComentarioFarmacia, Tnovedad, Novedad
from django.contrib import admin

# Register your models here.

class FarmaciaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_display =  ['nombre', 'reputacion', 'direccion', 'telefono', 'latitud', 'longitud', 'horario_atencion','estado']

class ComentarioFarmaciaAdmin(admin.ModelAdmin):
    search_fields = ['farmacia']
    list_filter = ['farmacia']
    list_display =  ['farmacia', 'observacion', 'calificacion', 'estado']

class TnovedadAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_filter = ['nombre']
    list_display =  ['nombre', 'estado']

class NovedadAdmin(admin.ModelAdmin):
    search_fields = ['farmacia', 'consecutivo', 'registro_invima']
    list_filter = ['farmacia']
    list_display =  ['farmacia', 'tnovedad', 'registro_invima', 'expediente', 'consecutivo', 'observacion','estado']

admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(ComentarioFarmacia, ComentarioFarmaciaAdmin)
admin.site.register(Tnovedad, TnovedadAdmin)
admin.site.register(Novedad, NovedadAdmin)