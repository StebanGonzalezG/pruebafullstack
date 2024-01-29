from django.urls import path
from .views import actualizar_datos, registrar_datos, historial_adquisiciones

urlpatterns = [
    path('registrar', registrar_datos, name='registrar_datos'),
    path('historial', historial_adquisiciones, name='historial_adquisiciones'),
    path('actualizar/<int:adquisicion_id>', actualizar_datos, name='actualizar_datos'),
]