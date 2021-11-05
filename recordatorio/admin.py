from django.contrib import admin

# Register your models here.
from django.contrib import admin

#Importamos la aplicacion
from .models import Recordatorio
# Register your models here.

#Aqui agregamos servicios al panel de administracion

class RecordatorioAdmin(admin.ModelAdmin):
    #Incluya campos de created y updated, solo lectura
    readonly_fields=('created', 'updated')


admin.site.register(Recordatorio, RecordatorioAdmin)