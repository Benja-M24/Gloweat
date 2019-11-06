from django.urls import path
from apps.productos.views import ProductoViewSet

urlpatterns = [
    path('list/', ProductoViewSet),
]

 