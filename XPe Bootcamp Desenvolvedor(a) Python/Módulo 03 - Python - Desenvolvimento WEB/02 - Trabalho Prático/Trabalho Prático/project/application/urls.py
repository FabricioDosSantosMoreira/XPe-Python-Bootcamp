from django.urls import path

from application.views import calcular_coeficientes, index

urlpatterns = [
    path('', index, name='index'),
    path('calcular/', calcular_coeficientes, name='calcular')
]
