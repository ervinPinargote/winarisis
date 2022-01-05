# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ConfiguracionIndex, noticias_index
from organizacionn.models import organizaciones
from productos.models import  presentacion


def index_principalF(request):
    inst = ConfiguracionIndex.objects.get(pk=1)
    noti = noticias_index.objects.all()
    orga = organizaciones.objects.all()
    productos = presentacion.objects.all()
    return render(request, 'index/index.html', {'inst1': inst, 'not2': noti, 'organizacion': orga, 'productos': productos, })


class index_principal(TemplateView):
    template_name = "index/index.html"
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirigir a una página de éxito.

    else:
        # Devuelve un mensaje de error de 'inicio de sesión no válido'.
        return render(request, 'index/index.html',)