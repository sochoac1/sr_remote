from django.db import models
from django.db.models.fields.related import ForeignKey
# Modelos de la busqueda

#Waste container
class Waste_Container(models.Model):
    name=models.CharField(max_length=100) 
    color=models.CharField(max_length=50)
    deposit_content=models.CharField(max_length=1500)
    image = models.ImageField(upload_to='waste_container', null=True, blank=True)
    #fecha de creacion
    created = models.DateTimeField(auto_now_add=True)
    #fecha de modificacion
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='waste_container' #Especificamos el nombre en la BD
        verbose_name_plural='waste_containers' 

    def __str__(self):
        return "%s" % (self.name)


#Solid waste
class Solid_Waste(models.Model):
    name=models.CharField(max_length=100)
    recycle_type=models.CharField(max_length=1500)
    material=models.CharField(max_length=50)
    waste_container= models.ManyToManyField(Waste_Container)
    image = models.ImageField(upload_to='solid_waste', null=True, blank=True)

    #fecha de creacion
    created = models.DateTimeField(auto_now_add=True)
    #fecha de modificacion
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='solid_waste' #Especificamos el nombre en la BD
        verbose_name_plural='solid_wastes'

    def __str__(self):
        return "%s " % (self.name)