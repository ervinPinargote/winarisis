from django.urls import path

from .views import index_principal, index_principalF, my_view, acerca_de, organizaciones_view, procudtos_view

urlpatterns = [
    #path('', index_principal.as_view(), name='index1'),
    path('/', index_principalF, name='index'),
    path('/login', my_view, name='login'),
    path('/acerca', acerca_de, name='acerca_de'),
    path('organizaciones', organizaciones_view, name='organizaciones_view'),
    path('productos', procudtos_view, name='procudtos_view'),

]
