from django.shortcuts import render

# Create your views here.
def starterpack(request):
    
    return render(request, "starterpack/starterpack.html")
