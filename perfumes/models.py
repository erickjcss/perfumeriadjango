from django.db import models
class Perfumes(models.Model):
    
    perfume=models.CharField(max_length=50)
    cantidad=models.CharField(max_length=20,default="100 ml")
    precioDolar=models.BooleanField(default=False)
    genero=models.CharField(default="",max_length=20)
    diminutivo=models.CharField(max_length=20,default='')
    disponible=models.BooleanField(default=True)
    precio=models.IntegerField(default="")
    casa=models.TextField(default='',blank=True)
    original=models.BooleanField(default=False)
    popular=models.BooleanField()
    acordesPrincipales=models.TextField(blank=True)
    acordePrincipal=models.CharField(max_length=30,blank=True)
    fotosReales=models.TextField(blank=True)
    fotosCatalogo=models.TextField(blank=True)   
    estacionesRecomendadas=models.TextField(default='',blank=True) 