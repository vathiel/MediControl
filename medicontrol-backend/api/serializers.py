from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from models import Farmacia, ComentarioFarmacia, Tnovedad, Novedad
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class FarmaciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmacia
        fields = ('nombre', 'reputacion', 'direccion', 'telefono', 'latitud', 'longitud', 'horario_atencion','estado')

class ComentarioFarmaciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComentarioFarmacia
        fields = ('farmacia', 'observacion', 'calificacion', 'estado')

class TnovedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tnovedad
        fields = ('nombre', 'estado')

# Serializers define the API representation.
class NovedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Novedad
        fields = ('farmacia', 'tnovedad', 'registro_invima', 'expediente', 'consecutivo', 'observacion','estado')
