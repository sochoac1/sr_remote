from busquedas.models import Solid_Waste
from django.shortcuts import render
from django.http import HttpResponse
from .models import Solid_Waste, Waste_Container
from django.db.models import CharField
from django.db.models.functions import Lower

CharField.register_lookup(Lower)
# Create your views here.

def busquedas(request):
    
    return render(request, "busquedas/busquedas.html")
    

def smart_search(request):

    if request.method == "POST":
        searched = request.POST['searched']

        residuos = Solid_Waste.objects.filter(name__icontains=searched)

        return render(request, "busquedas/sm_result.html", {'searched': searched, 'residuos': residuos}) 

    else:
        return render(request, "busquedas/smart_search.html") 

#Metodo que muestra en que caneca tirar de smart search
def show_sm(request, residuo_id):

    #Tomamos objeto con es pk
    residuo = Solid_Waste.objects.get(pk=residuo_id) 
    

    return render(request, 'busquedas/show_sm.html',{'residuo':residuo})

#Metodo de reycle search
def recycle_search(request):

    if request.method == "POST":
        searched = request.POST['searched']

        residuos = Solid_Waste.objects.filter(name__icontains=searched)

        return render(request, "busquedas/rm_result.html", {'searched': searched, 'residuos': residuos}) 

    else:
        return render(request, "busquedas/recycle_search.html") 

#Metodo que muestra modo de reciclaje
def show_rm(request, residuo_id):

    #Tomamos objeto con es pk
    residuo = Solid_Waste.objects.get(pk=residuo_id) 
    

    return render(request, 'busquedas/show_rm.html',{'residuo':residuo})

#Metodo para mostrar los tipos de basura
def clean_container(request):

    #Importar servicios del panel de Admin, luego decirle a vista de Servicios que los muestre

    #Importar archivo servicios: Necesito acceder a cada campo
    containers = Waste_Container.objects.all() #Importe todos los objetos construidos

    #Render devuelva plantilla renderizada y servicios importados
    return render(request, "busquedas/clean_container.html",{ "containers": containers})