from django.urls import path

from .views import OrganizacionIndexList, cRedesSociales, cAutoridadesViews

urlpatterns = [
    path('organizacion/<int:pk>/', OrganizacionIndexList.as_view(), name='OrganizacionIndex'),
    path('organizacion/redes/<int:id_organizacion>/', cRedesSociales, name='detail'),
    path('organizacion/autoridades/<int:id_organizacion>/', cAutoridadesViews, name='detailAut'),
    # path('matriculas/adm/est/', CAdmisionListaEstudiante, name='ListAdm'),
    #
    # path('matricula/estudiante/ficha/(?P<pk>\d+)/$', MatriculaFicha.as_view(), name="MatriculaFicha"),

    # Reportes URLS

    # path('matricula/pdf/(?P<pk>\d+)/',pdfMatricula_view.as_view(),name='ReporteMatricula'),
]
