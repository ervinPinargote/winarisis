import datetime
import os


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views import View
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from uri.part import user
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



from organizacionn.models import usuarios_organizacion, organizaciones
from productos.models import producto, presentacion, calificacion

from productos.forms import AgregarProductosForm, AgregarPresentacionesProductosForm, CalificarProductosForm, \
    EditarProductosForm, EditarPresentacionesProductosForm

from administracion.models import ConfiguracionIndex, noticias_index

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
    noti = noticias_index.objects.all()
    productos = presentacion.objects.all()[:5]
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
        'not2': noti,
        'productos': productos,
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



class FichaAdmisionPDF_view(View):
    def link_callback(self, uri, rel):
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri
        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        presentacion1 = presentacion.objects.all()
        #admision = admisione.objects.get(pk=self.kwargs['pk']) #obtener la admission.
        #estudios = estudios_realizado.objects.all().filter(ci=admision.ci.ci)
        #user = User.objects.get(
        #    username=self.request.user)  # envia el usuario que esta en la logueado en la aplicacion.
        reporte_name = "reporte"
        template_path = 'reportes/reporte1.html'
        fecha = datetime.date.today()
        context = {'tittle': 'CATÁLOGO DE PRODUCTOS ', 'admision': '01',
                   'items': presentacion1,
                   'codigo': 100,
                   'icon': '{}{}'.format(settings.MEDIA_URL, 'el-coca.jpg'),
                   'estudios': 100,
                   'date': fecha
                   #'usuario': user
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + reporte_name + ".pdf"
        template = get_template(template_path)
        html = template.render(context)
        if request.POST.get('show_html', ''):
            response['Content-Type'] = 'application/text'
            response['Content-Disposition'] = 'attachment; filename="ABC.txt"'
            response.write(html)
        else:
            pisaStatus = pisa.CreatePDF(
                html.encode("UTF-8"), dest=response, link_callback=self.link_callback)
            if pisaStatus.err:
                return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err, html))
        return response


class ReporteUsuario_view(View):
    def link_callback(self, uri, rel):
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL  # Typically /static/
            sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL  # Typically /media/
            mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri
        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        usuarios_registrados = User.objects.filter(groups__name='usuario_calificador')
        #admision = admisione.objects.get(pk=self.kwargs['pk']) #obtener la admission.
        #estudios = estudios_realizado.objects.all().filter(ci=admision.ci.ci)
        #user = User.objects.get(
        #    username=self.request.user)  # envia el usuario que esta en la logueado en la aplicacion.
        reporte_name = "reporte_usuarios"
        template_path = 'reportes/usuarios.html'
        fecha = datetime.date.today()
        context = {'tittle': 'USUARIOS WIÑARI WEB ', 'admision': '01',
                   'users': usuarios_registrados,
                   'codigo': 100,
                   'icon': '{}{}'.format(settings.MEDIA_URL, 'el-coca.jpg'),
                   'estudios': 100,
                   'date': fecha
                   #'usuario': user
                   }
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + reporte_name + ".pdf"
        template = get_template(template_path)
        html = template.render(context)
        if request.POST.get('show_html', ''):
            response['Content-Type'] = 'application/text'
            response['Content-Disposition'] = 'attachment; filename="ABC.txt"'
            response.write(html)
        else:
            pisaStatus = pisa.CreatePDF(
                html.encode("UTF-8"), dest=response, link_callback=self.link_callback)
            if pisaStatus.err:
                return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err, html))
        return response
