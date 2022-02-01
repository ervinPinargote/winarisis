# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'content': {'message': 'Exito al Iniciar Sesion', 'color': 'succes',
                                                 'nota': 'Bienvenido!!!',
                                                 }})
        else:
            return JsonResponse({'content': {'message': 'Error al Iniciar Sesion', 'color': 'danger',
                                             'nota': 'usuario o contraseña incorrectas!!!',
                                             }})
    else:
        form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def acerca_de(request):
    inst = ConfiguracionIndex.objects.get(pk=1)
    noti = noticias_index.objects.all()
    orga = organizaciones.objects.all()[:5]
    productos = presentacion.objects.all()
    return render(request, 'index/about.html', {'inst1': inst, 'not2': noti, 'organizacion': orga, 'productos': productos, })


def organizaciones_view(request):
    inst = ConfiguracionIndex.objects.get(pk=1)
    noti = noticias_index.objects.all()
    orga = organizaciones.objects.all()
    productos = presentacion.objects.all()[:5]
    return render(request, 'index/organizaciones.html', {'inst1': inst, 'not2': noti, 'organizacion': orga, 'productos': productos, })

def procudtos_view(request):
    inst = ConfiguracionIndex.objects.get(pk=1)
    noti = noticias_index.objects.all()
    orga = organizaciones.objects.all()
    productos = presentacion.objects.all()[:5]
    return render(request, 'index/product_all.html', {'inst1': inst, 'not2': noti, 'organizacion': orga, 'productos': productos, })