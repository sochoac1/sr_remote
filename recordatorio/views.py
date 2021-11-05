from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User

from recordatorio.forms import RecordatorioForm
from recordatorio.models import Recordatorio

# Create your views here.

def recordatorio(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = RecordatorioForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False) 
            reminder.user = current_user 
            reminder.save()
            return redirect('Recordatorios')
    else:
        form = RecordatorioForm()
    return render(request, 'recordatorio/recordatorio.html',{'form': form})


def mostrarRecordatorios(request):
    
    recordatorios = Recordatorio.objects.filter(user=request.user) #Importe todos los objetos construidos

    #Render devuelva plantilla renderizada y servicios importados
    return render(request, "recordatorio/mostrar.html",{ "recordatorios": recordatorios})
