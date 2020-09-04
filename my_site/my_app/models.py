from django.db import models
from django import forms

# Create your models here.

class categorie(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class crepe(models.Model):
    name= models.CharField(max_length=100 )
    cat=models.ForeignKey(categorie,on_delete=models.CASCADE,related_name='type')
    ingredients=models.CharField(max_length=200)
    prix = models.FloatField()
    img=models.ImageField(upload_to='app',default='media/default.png')

    def __str__(self):
        return self.name

class point_de_vente(models.Model):
    adresse=models.CharField(max_length=50)
    def __str__(self):
        return self.adresse

class livraison(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class clients(models.Model):
    name = models.CharField(max_length=100)
    num = models.IntegerField(blank=True, null=True)
    commande=models.ManyToManyField(crepe,blank=True)
    mode_de_livraison=models.ManyToManyField(livraison,blank=True)
    point_de_vente=models.ForeignKey(point_de_vente,on_delete=models.CASCADE , blank=True , null=True)
   
    def __str__(self):
        return self.name
    


















