from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from models import Farmacia, ComentarioFarmacia
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class FarmaciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Farmacia
        fields = ('nombre', 'reputacion', 'direccion')

class ComentarioFarmaciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComentarioFarmacia
        fields = ('farmacia', 'observacion', 'calificacion')
