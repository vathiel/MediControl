from rest_framework import routers, serializers, viewsets
from views import UserViewSet, FarmaciaViewSet, ComentarioFarmaciaViewSet

from django.conf.urls import url, include
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'farmacias', FarmaciaViewSet)
router.register(r'comentarios-farmacia', ComentarioFarmaciaViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
