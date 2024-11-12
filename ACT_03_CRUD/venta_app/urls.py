from django.urls import path
from venta_app import views

urlpatterns = [
    path('',views.inicio_vista,name='inicio_vista'),
    path('registrarVenta/',views.registrarVenta,name="registrarVenta"),
    path('seleccionarVenta/<idventa>',views.seleccionarVenta,name='seleccionarVenta'),
    path('editarVenta/<idventa>',views.editarVenta,name='editarVenta'),
    path('borrarVenta/<idventa>',views.borrarVenta,name='borrarVenta'),
]
