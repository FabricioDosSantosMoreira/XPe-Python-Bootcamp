from django.urls import path

from application.views import create, delete, index, refresh

urlpatterns = [
    path('', index, name='index'),
    path('criar/', create, name='criar'),
    path('modificar/<int:user_id>', refresh, name='modificar'),
    path('deletar/<int:user_id>', delete, name='deletar'),
]
