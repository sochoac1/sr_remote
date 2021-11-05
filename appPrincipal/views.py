from django.shortcuts import render, HttpResponse
#Importar HttpResponse

# Create your views here.

#Inicio
def home(request):

    return render(request, "appPrincipal/home.html")