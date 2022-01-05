from django.urls import path

from .views import index_principalF, index_organizacion, productos_organizacion, agregar_productos_organizacion, \
    presentacion_productos_organizacion, agregar_presentacion_productos, presentacion_productos_todos_organizacion, \
    presentacion_productos_cliente

urlpatterns = [
    #path('', index_principal.as_view(), name='index1'),
    path('index', index_principalF, name='indexOrganizacion'),
    path('organizacion/(?P<id_organizacion>\d+)/$', index_organizacion, name='index_organizacion'),
    #path('organizacion/productos/(?P<id_organizacion>\d+)/$', productos_organizacion, name='productos_organizacion'),

    path('organizacion/productos/<int:id_organizacion>/', productos_organizacion, name='productos_organizacion'),
    path('organizacion/productos/agregar/<int:id_organizacion>/', agregar_productos_organizacion, name='agregar_productos_organizacion'),
    path('organizacion/productos/presentacion/<int:id_producto>/', presentacion_productos_organizacion, name='presentacion_productos_organizacion'),
    path('organizacion/productos/agregar/presentacion/<int:id_producto>/', agregar_presentacion_productos, name='agregar_presentacion_productos'),

    path('organizacion/productos/todas/presentacion/<int:id_organizacion>/', presentacion_productos_todos_organizacion, name='todas_presentacion_productos'),




    path('productos/presentacion/<int:id_presentacion>/', presentacion_productos_cliente, name='presentacion_productos_cliente'),
]
