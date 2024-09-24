from django.urls import path, include
from rest_framework import routers

from order import viewsets

route = routers.SimpleRouter()
route.register(r'order', viewsets.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(route.urls)),
]
