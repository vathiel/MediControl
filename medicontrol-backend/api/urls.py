from rest_framework import routers, serializers, viewsets
from views import UserViewSet, FarmaciaViewSet, ComentarioFarmaciaViewSet, TnovedadViewSet, NovedadViewSet

from django.conf.urls import url, include
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'farmacias', FarmaciaViewSet)
router.register(r'comentarios-farmacia', ComentarioFarmaciaViewSet)
router.register(r'tnovedad', TnovedadViewSet)
router.register(r'novedad', NovedadViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
