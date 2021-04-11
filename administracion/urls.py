from django.urls import path

from .views import index_principal, index_principalF

urlpatterns = [
    path('', index_principal.as_view(), name='index'),
    path('as/', index_principalF, name='index1'),

]
