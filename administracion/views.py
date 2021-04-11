# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ConfiguracionIndex

def index_principalF(request):
    inst = ConfiguracionIndex.objects.get(pk=1)
    return render(request, 'index/index.html', {'inst': inst})


class index_principal(TemplateView):
    template_name = "index/index.html"


