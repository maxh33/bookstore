from os.path import basename

from django.urls import path, include
from rest_framework import routers

from bookstore.urls import urlpatterns
from product import viewsets

router = routers.SimpleRouter()
router.register(r'product', viewsets.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
