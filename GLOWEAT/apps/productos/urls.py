from apps.productos.views import ProductoViewSet, PedidoViewSet, ConsultaProductosEstado
from apps.productos.api import UserAPI
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'prod', ProductoViewSet, base_name='prod')
router.register(r'pedidos', PedidoViewSet, base_name='cocina')
router.register(r'cons', ConsultaProductosEstado, base_name='consulta')
urlpatterns = router.urls
