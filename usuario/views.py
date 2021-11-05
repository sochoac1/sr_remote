from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth import login
# Create your views here.

def registro(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            form.save()
            login(request, user)           
            return redirect('Home')
        
    else:
        form = UserRegisterForm()
      
          
    return render(request, 'usuario/registro.html',{'form': form})