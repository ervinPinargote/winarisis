from django.urls import path

from .views import RegistroUsuario, Registro_usuario_perms, logout

urlpatterns = [
    #path('registrar/', RegistroUsuario.as_view(), name='registrar'),
    path('registrar/', Registro_usuario_perms, name='registrar'),
    path('salir/', logout, name='salir'),
]
