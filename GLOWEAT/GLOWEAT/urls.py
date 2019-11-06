from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('crear_usuario/', CrearUsuario, name='crear_usuario'),
    path('prod/', include('apps.productos.urls')),
]
