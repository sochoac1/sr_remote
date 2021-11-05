from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

#Solid Waste
class Waste_Container(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    deposit_content=models.CharField(max_length=1500)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='waste_container', null=True, blank=True)
    class Meta:
        verbose_name='waste_container'
        verbose_name_plural='wast_containers'
    def __str__(self):
        return "%s" %(self.name)
        
class Solid_Waste(models.Model):
    name=models.CharField(max_length=100)
    recycle_type=models.CharField(max_length=1500)
    material=models.CharField(max_length=50)
    waste_container=models.ManyToManyField(Waste_Container)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='solid_waste',null=True, blank=True)
    impact=models.CharField(max_length=6,null=True, blank=True)
    class Meta:
        verbose_name='solid_waste'
        verbose_name_plural='solid_wastes'
    def __str__(self):
        return "%s" %(self.name)

