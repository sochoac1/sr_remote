from django.contrib import admin
from .models import Solid_Waste, Waste_Container

# Register your models here.
class Solid_Waste_Admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class Waste_Container_Admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Solid_Waste, Solid_Waste_Admin)
admin.site.register(Waste_Container, Waste_Container_Admin)