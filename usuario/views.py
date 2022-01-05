
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.views.generic import CreateView


from .forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "login/registro_modal.html"
    form_class = RegistroForm
    success_url = './'
    # guarde asige directa al grupo.

def Registro_usuario_perms(request):
    if request.session.get('id') != None:  # Regístrese solo cuando no haya iniciado sesión
        return redirect('/')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            message = 'este nombre de usuario ha sido registrado'
            return render(request, 'login/registro_modal.html', {"message": message})
        user = User()
        user.username = username
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        user.groups.add(2) ## ESCOGEMOS AL GRUPO QUE PUEDE INICIAR
        request.session['id'] = user.id  # Registrar que el usuario ha iniciado sesión
        return redirect('/')
    return render(request, 'login/registro_modal.html')

def logout(request):
    request.session.flush()
    return redirect('inicio')