from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('registro/',views.registro, name='registro'),
    
]

