from django.urls import path 
#from apps.autos.views import lista_autos, agregar_auto, detalle_auto, editar_auto, eliminar_auto
from .views import *

urlpatterns = [
    path('lista/', lista_autos, name='lista_autos'),
    path('agregar/', agregar_auto, name='agregar_auto'),
    path('detalle/<int:id_auto>/', detalle_auto, name='detalle_auto'),
    path('editar/<int:id_auto>/', editar_auto, name='editar_auto'),
    path('eliminar/<int:id_auto>/', eliminar_auto, name='eliminar_auto'),

    path('lista_marca/', lista_marcas, name='lista_marcas'),
    path('agregar_marca/', agregar_marca, name='agregar_marca'),
    path('detalle_marca/<int:id_marca>/', detalle_marca, name='detalle_marca'),
    path('editar_marca/<int:id_marca>/', editar_marca, name='editar_marca'),
    path('eliminar_marca/<int:id_marca>/', eliminar_marca, name='eliminar_marca'),

    path('login/', vista_login, name='login'),
    path('logout/', vista_logout, name='logout'),

]