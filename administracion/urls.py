from django.urls import path

from .views import index_principal, index_principalF, my_view

urlpatterns = [
    #path('', index_principal.as_view(), name='index1'),
    path('/', index_principalF, name='index'),
    path('/login', my_view, name='login'),

]
