from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import organizaciones, redes_sociales, autoridades_organizacion
from administracion.models import ConfiguracionIndex


class OrganizacionIndexList(ListView):
    model = organizaciones
    template_name = 'organizaciones/index_organizacion.html'

    def get_context_data(self, **kwargs):
        idorganizacion = self.kwargs['pk']
        orga = organizaciones.objects.get(pk=idorganizacion)
        inst = ConfiguracionIndex.objects.get(pk=1)
        ac = 0
        ne = 0
        context = super(OrganizacionIndexList, self).get_context_data(**kwargs)
        context['organizaciones'] = orga
        context['Titulo'] = "Organizaciones"
        context['inst1'] = inst
        return context


def cRedesSociales(request, id_organizacion):
    redes = redes_sociales.objects.all().filter(id_organizacion=id_organizacion).order_by('-id')
    contexto = {'redes': redes}
    return render(request, 'organizaciones/redes_sociales_organizacion.html', contexto)


def cAutoridadesViews(request, id_organizacion):
    aut = autoridades_organizacion.objects.all().filter(id_organizacion=id_organizacion).order_by('-id')
    contexto = {'autoridades': aut}
    return render(request, 'organizaciones/autoridades_organizacion.html', contexto)
