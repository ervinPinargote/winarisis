from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from organizacionn.models import usuarios_organizacion, organizaciones
from productos.models import producto, presentacion, calificacion

from productos.forms import AgregarProductosForm, AgregarPresentacionesProductosForm, CalificarProductosForm, \
    EditarProductosForm, EditarPresentacionesProductosForm

from administracion.models import ConfiguracionIndex

from organizacionn.forms import EditarOrganizacionForm


@login_required
def index_principalF(request):
    #  inst = ConfiguracionIndex.objects.get(pk=1)
    #  noti = noticias_index.objects.all()
    #  orga = organizaciones.objects.all()
    user = User.objects.get(username=request.user)
    Organizacions = usuarios_organizacion.objects.all().filter(id_usuarios=user.id)
    contexto = {'oranizaciones': Organizacions}
    return render(request, 'productos_admin/index.html', contexto)


def index_organizacion(request, id_organizacion):
    Organizacion = organizaciones.objects.get(id=id_organizacion)
    contexto = {'Organizacion': Organizacion}
    return render(request, 'productos_admin/index_organizacion.html', contexto)


def productos_organizacion(request, id_organizacion):
    Organizacion = organizaciones.objects.get(id=id_organizacion)
    Productos = producto.objects.all().filter(id_organizacion=id_organizacion)

    contexto = {'Organizacion': Organizacion,
                'Productos': Productos
                }
    return render(request, 'productos_admin/organizacion_productos.html', contexto)


def agregar_productos_organizacion(request, id_organizacion):
    if request.method == 'POST':
        saldopendiente = request.POST.get("Valor_pendiente")
        valpagado = request.POST.get("valor_cancelado")
        form = AgregarProductosForm(request.POST)
        if form.is_valid():
            if form.save():
                mensaje = "Guardado con exito"
        return redirect('adminOrganiacion:productos_organizacion', id_organizacion)
    else:
        form = AgregarProductosForm()
    contexto = {'message': 'Guardado con Exito',
                'form': form,
                'id_organizacion': id_organizacion,
                }
    return render(request, 'productos_admin/modal_agregar_productos.html', contexto)


def presentacion_productos_organizacion(request, id_producto):
    Producto = producto.objects.get(id=id_producto)  # Encuentro el Producto.
    # Organizacion = organizaciones.objects.get(id=Productos.id_organizacion.id) #Ecuentro La Organizacion
    Presentaciones = presentacion.objects.all().filter(id_producto=id_producto)  # Encontramos las Presentaciones

    contexto = {'Producto': Producto,
                'Presentaciones': Presentaciones
                }
    return render(request, 'productos_admin/presentacion_productos.html', contexto)


def agregar_presentacion_productos(request, id_producto):
    if request.method == 'POST':
        saldopendiente = request.POST.get("Valor_pendiente")
        valpagado = request.POST.get("valor_cancelado")
        form = AgregarPresentacionesProductosForm(request.POST, request.FILES)
        if form.is_valid():
            if form.save():
                mensaje = "Guardado con exito"
        return redirect('adminOrganiacion:presentacion_productos_organizacion', id_producto)
    else:
        form = AgregarPresentacionesProductosForm()
    contexto = {'message': 'Guardado con Exito',
                'form': form,
                'id_producto': id_producto,
                }
    return render(request, 'productos_admin/modal_agregar_presentacion.html', contexto)


def presentacion_productos_todos_organizacion(request, id_organizacion):
    # Producto = producto.objects.get(id=id_producto) #Encuentro el Producto.
    Organizacion = organizaciones.objects.get(id=id_organizacion)  # Ecuentro La Organizacion
    # Presentaciones = presentacion.objects.all().filter(id_producto.id_organizacion.id=id_organizacion) #
    # Encontramos las Presentaciones
    Presentaciones = presentacion.objects.select_related().filter(
        id_producto__id_organizacion=id_organizacion)  # Encontramos las Presentaciones
    # book = Book.objects.select_related('person__city').filter(pk=1)

    contexto = {
        'Organizacion': Organizacion,
        'id_organizacion': id_organizacion,
        'Presentaciones': Presentaciones,
    }
    return render(request, 'productos_admin/todas_presentaciones_productos.html', contexto)


def presentacion_productos_cliente(request, id_presentacion):
    inst = ConfiguracionIndex.objects.get(pk=1)
    Presentacion = presentacion.objects.get(id=id_presentacion)  # Encontramos las Presentaciones
    Calificaciones = calificacion.objects.all().filter(id_presentacion=id_presentacion)
    # book = Book.objects.select_related('person__city').filter(pk=1)
    total = 0
    cal = 0
    if len(Calificaciones) > 0:
        for tot in Calificaciones:
            total = total + tot.porcentaje
        cal = total / len(Calificaciones)

    contexto = {
        'inst1': inst,
        'id_presentacion': id_presentacion,
        'pr': Presentacion,
        'calificaciones': Calificaciones,
        'numestrellas': round(cal),
        'ne': len(Calificaciones),
    }
    return render(request, 'index/product.html', contexto)


def calificacion_productos_cliente(request, id_presentacion):
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        saldopendiente = request.POST.get("Valor_pendiente")
        valpagado = request.POST.get("valor_cancelado")
        form = CalificarProductosForm(request.POST)
        if form.is_valid():
            if form.save():
                mensaje = "Guardado con exito"
        return redirect('adminOrganiacion:presentacion_productos_cliente', id_presentacion)
    else:
        form = CalificarProductosForm()
    contexto = {'message': 'Guardado con Exito',
                'form': form,
                'id_presentacion': id_presentacion,
                'user': user,
                }
    return render(request, 'productos_calificacion/modal_calificacion.html', contexto)


# EDITAR LA INFORMACION DE UN PRODUCTO
def CproductoEditarModal(request, id_producto):
    product = producto.objects.get(id=id_producto)
    if (request.method == 'GET'):
        form = EditarProductosForm(instance=product)
    else:
        form = EditarProductosForm(request.POST, instance=product)
        if form.is_valid():
            if form.save():
                error = "Datos Actulizados Correctamente!!!"
                # return redirect('academia:Listar')  # Redirijo a la Listar que es Principal en el funcionalidad
                return JsonResponse({'content': {'message': error, 'color': '1', }})
        else:
            error = "Error en la Actulizacion de Datos!!!"
            # return redirect('academia:Listar')  # Redirijo a la Listar que es Principal en el funcionalidad
            return JsonResponse({'content': {'message': error, 'color': '0', }})
    return render(request, 'productos_admin/modal_editar_productos.html',
                  {'form': form, 'title': "Editar", 'id': id_producto})


# EDITAR LA INFORMACION DE LA ORGANIZACION

def CorganizacionEditarModal(request, id_organizacion):
    organizaci = organizaciones.objects.get(id=id_organizacion)
    if (request.method == 'GET'):
        form = EditarOrganizacionForm(instance=organizaci)
    else:
        form = EditarOrganizacionForm(request.POST, instance=organizaci)
        if form.is_valid():
            if form.save():
                error = "Datos Actulizados Correctamente!!!"
                # return redirect('academia:Listar')  # Redirijo a la Listar que es Principal en el funcionalidad
                return JsonResponse({'content': {'message': error, 'color': '1', }})
        else:
            error = "Error en la Actulizacion de Datos!!!"
            # return redirect('academia:Listar')  # Redirijo a la Listar que es Principal en el funcionalidad
            return JsonResponse({'content': {'message': form.errors, 'color': '0', }})
    return render(request, 'productos_admin/modal_editar_organizacion.html',
                  {'form': form, 'title': "Editar", 'id': id_organizacion})

# EDITAR LA INFORMACION DE UN PRODUCTO
def CpresentacionEditarModal(request, id_presentacion):
    presentac = presentacion.objects.get(id=id_presentacion)
    if (request.method == 'GET'):
        form = EditarPresentacionesProductosForm(instance=presentac)
    else:
        form = EditarPresentacionesProductosForm(request.POST, instance=presentac)
        if form.is_valid():
            if form.save():
                error = "Datos Actulizados Correctamente!!!"
                # return redirect('academia:Listar')  # Redirijo a la Listar que es Principal en el funcionalidad
                return JsonResponse({'content': {'message': error, 'color': '1', }})
        else:
            error = "Error en la Actulizacion de Datos!!!"
            # return redirect('academia:Listar')  # Redirijo a la Listar que es Principal en el funcionalidad
            return JsonResponse({'content': {'message': error, 'color': '0', }})
    return render(request, 'productos_admin/modal_editar_presentacion.html',
                  {'form': form, 'title': "Editar", 'id': id_presentacion})