from typing import Container
from busquedas.models import Solid_Waste
from django.shortcuts import render
from django.http import HttpResponse
from .models import Solid_Waste, Waste_Container
# Create your views here.
def busquedas(request):
    
    return render(request, "busquedas/busqueda.html")

#Metodo de donde botar una basura
def smart_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        residuos = Solid_Waste.objects.filter(name__icontains=searched)
        return render(request, "busquedas/sm_result.html", {'searched': searched, 'residuos': residuos}) 
    else:
        return render(request, "busquedas/smart_search.html")

#Mostrar las canecas correspondientes
def show_sm(request, residuo_id):
    residuo = Solid_Waste.objects.get(pk=residuo_id)
    return render(request,'busquedas/show_sm.html',{'residuo':residuo})

#Metodo de busqueda de reciclaje
def recycle_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        residuos = Solid_Waste.objects.filter(name__icontains=searched)
        return render(request, "busquedas/rm_result.html", {'searched': searched, 'residuos': residuos}) 
    else:
        return render(request, "busquedas/recycle_search.html")

#Mostar la forma de reciclaje
def show_rm(request, residuo_id):
    residuo = Solid_Waste.objects.get(pk=residuo_id)
    return render(request,'busquedas/show_rm.html',{'residuo':residuo})

def clean_container(request):
    container = Waste_Container.objects.all()
    return render(request, "busquedas/clean_container.html",{'containers':container})