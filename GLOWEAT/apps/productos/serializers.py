from rest_framework import serializers
from apps.productos.models import productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = ('id_producto', 'nombre', 'descripcion', 'precioVenta')