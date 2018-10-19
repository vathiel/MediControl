# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from serializers import UserSerializer, FarmaciaSerializer, ComentarioFarmaciaSerializer, NovedadSerializer, TnovedadSerializer
from django.shortcuts import render
from models import Farmacia, ComentarioFarmacia, Tnovedad, Novedad
# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class FarmaciaViewSet(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer

# ViewSets define the view behavior.
class ComentarioFarmaciaViewSet(viewsets.ModelViewSet):
    queryset = ComentarioFarmacia.objects.all()
    serializer_class = ComentarioFarmaciaSerializer

# ViewSets define the view behavior.
class TnovedadViewSet(viewsets.ModelViewSet):
    queryset = Tnovedad.objects.all()
    serializer_class = TnovedadSerializer

# ViewSets define the view behavior.
class NovedadViewSet(viewsets.ModelViewSet):
    queryset = Novedad.objects.all()
    serializer_class = NovedadSerializer