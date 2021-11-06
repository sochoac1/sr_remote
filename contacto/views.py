from django.shortcuts import render, redirect
#Importamos el formularioCOntacto
from .forms import FormularioContacto 
from django.core.mail import EmailMessage

# Create your views here.

#Contacto
def contacto(request):
    formulario_contacto=FormularioContacto()
    #Si el usuario ha hecho post
    if request.method=="POST":
        #Rescata informacion que habia en el formulario.
        #Carga informacion en el formulario contacto y pasarle por parametro al constructor
        #los datos.
        #Cargamos en nuestro formulario la informacion que el usuario ha ido cargando. Para rescatar cada campo del formulario.
        formulario_contacto=FormularioContacto(data=request.POST)

        #Si formulario es valido. Se relleno todo
        if formulario_contacto.is_valid():
            #Rescato lo que tengo en cada campo
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            
            email=EmailMessage("Mensaje desde app Django", 
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
            "", ["smartrecycle.12@gmail.com"], reply_to=[email]
            )

            #Coordinamos en caso de error
            try:
                email.send()

                #Redireccione url pasandole un parametro
                return redirect("Home")

            except:

                return redirect('Home')

    return render(request, "contacto/contacto.html", {"miformulario":formulario_contacto})
