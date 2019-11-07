from apps.productos.views import ProductoViewSet, PedidoViewSet
from apps.productos.api import UserAPI
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'prod', ProductoViewSet, base_name='prod')
router.register(r'pedidos', PedidoViewSet, base_name='cocina')
urlpatterns = router.urls
