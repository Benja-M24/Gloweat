from apps.productos.views import ProductoViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'prod', ProductoViewSet, base_name='prod')
#router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
 