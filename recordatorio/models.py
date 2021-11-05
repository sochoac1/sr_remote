from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from . import myFields

# Create your models here.
#Creamos mapeo ORM

DAY_CHOICES = (
    ("Lunes", "Lunes"),
    ("Martes", "Martes"),
    ("Miercoles", "Miercoles"),
    ("Jueves", "Jueves"),
    ("Viernes", "Viernes"),
    ("Sabado", "Sabado"),
    ("Domingo", "Domingo"),
)


class Recordatorio(models.Model):
    #Campos recordatorio
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=1000)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reminders')
    hora = models.TimeField(auto_now=False, auto_now_add=False)
    diaSemana =  models.CharField(max_length=9,
                  choices=DAY_CHOICES,
                  default="martes")


    #Campos ordenar fecha y actualizacion
    #fecha creacion
    created = models.DateField(auto_now_add=True)
    #fecha de modificacion
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='recordatorio' #Especificamos el nombre en la BD
        verbose_name_plural='recordatorio'
    
    def __str__(self):
        return f'{self.user.username}: {self.diaSemana}'