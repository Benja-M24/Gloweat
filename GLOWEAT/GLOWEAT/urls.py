from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from apps.login.views import CrearUsuario, ListarUsuarios

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/' ,include(('apps.login.urls', 'Usuario'))),
    #path('home/' ,Home , name= 'login/login.html'),
    path('crear_usuario/', CrearUsuario, name='crear_usuario'),
    path('Listar_Usuarios/', ListarUsuarios, name='Listar_Usuarios'),
    path('prod/', include('apps.productos.urls')),
    path('accounts/',include('apps.accounts.urls')),
]

#if settings.DEBUG:
#   urlpatterns += [url(r'^media/(?P<path>.*)$'serve, {'document_root': settings.MEDIA_ROOT,}),]