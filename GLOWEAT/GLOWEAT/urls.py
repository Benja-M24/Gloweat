from django.contrib import admin
from django.urls import path, include
from apps.productos.api import UserAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prod/', include('apps.productos.urls')),
    path('user/', UserAPI.as_view(), name= "usuarios"),
]
