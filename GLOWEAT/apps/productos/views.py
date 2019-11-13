from rest_framework import viewsets
from apps.productos.models import productos, Pedido
from apps.productos.serializers import ProductoSerializer, PedidoSerializer


class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    model = productos
    queryset = productos.objects.all()
    serializer_class = ProductoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    model = Pedido
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# class ConsultaViewSet(viewsets.ModelViewSet):
#     model = Pedido
#     queryset = Pedido.objects.all()
#     serializer_class = ConsultaSerializer

class ConsultaProductosEstado(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = productos.objects.all()
    