from django.urls import path
#from . import views
from apps.productos.views import list_prod, crear_prod, editar_prod, borrar_prod

urlpatterns = [
    path('list/', list_prod,name="listar_url"),
    path('nuevo/', crear_prod,name="nuevo_url"),
    path('update/<int:id>', editar_prod,name="update_url"),
    path('delete/<int:id>', borrar_prod,name="delete_url"),
]

 