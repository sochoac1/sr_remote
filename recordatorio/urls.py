from django.urls import path
from . import views

urlpatterns = [

    path('crear/', views.recordatorio, name='crear'),
    path('', views.mostrarRecordatorios, name ='Recordatorios'),
]
