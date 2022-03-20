from django.urls import path

from .views import index_principalF, index_organizacion, productos_organizacion, agregar_productos_organizacion, \
    presentacion_productos_organizacion, agregar_presentacion_productos, presentacion_productos_todos_organizacion, \
    presentacion_productos_cliente, calificacion_productos_cliente, CproductoEditarModal, CorganizacionEditarModal, \
    CpresentacionEditarModal, FichaAdmisionPDF_view, ReporteUsuario_view

urlpatterns = [
    #path('', index_principal.as_view(), name='index1'),

    path('index', index_principalF, name='indexOrganizacion'),
    #ORGANIZACION
    path('organizacion/(?P<id_organizacion>\d+)/$', index_organizacion, name='index_organizacion'),
    path('organizacion/editar/(?P<id_organizacion>\d+)/$', CorganizacionEditarModal, name='editar_organizacion'),
    #path('organizacion/productos/(?P<id_organizacion>\d+)/$', productos_organizacion, name='productos_organizacion'),

    path('organizacion/productos/<int:id_organizacion>/', productos_organizacion, name='productos_organizacion'),

    # CRUD DE PRODUCTOS DE ORGANIZACION
    path('organizacion/productos/agregar/<int:id_organizacion>/', agregar_productos_organizacion, name='agregar_productos_organizacion'),
    path('organizacion/productos/editar/<int:id_producto>/', CproductoEditarModal, name='editar_productos_organizacion'),



    path('organizacion/productos/presentacion/<int:id_producto>/', presentacion_productos_organizacion, name='presentacion_productos_organizacion'),

    # CRUD DE PRESENTACIONES DE PRODCUTOS.
    path('organizacion/productos/agregar/presentacion/<int:id_producto>/', agregar_presentacion_productos, name='agregar_presentacion_productos'),
    path('organizacion/productos/editar/presentacion/<int:id_presentacion>/', CpresentacionEditarModal, name='editar_presentacion_productos'),


    path('organizacion/productos/todas/presentacion/<int:id_organizacion>/', presentacion_productos_todos_organizacion, name='todas_presentacion_productos'),
    path('productos/presentacion/<int:id_presentacion>/', presentacion_productos_cliente, name='presentacion_productos_cliente'),

    path('productos/presentacion/calificar/<int:id_presentacion>/', calificacion_productos_cliente, name='calificacion_productos_cliente'),

     # REPORTES PDF DE PRODUCTOS

     path('productos/pdf/<int:pk>/', FichaAdmisionPDF_view.as_view(), name='ReporteProductos'),
     path('usuarios/pdf/<int:pk>/', ReporteUsuario_view.as_view(), name='ReporteUsuario'),
]
