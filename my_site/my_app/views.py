from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_app.models import menu, categorie, clients
from .formulaire import menuu, validation 


# Create your views here.
adresses=['Menzah5','Aouina']


def index(request):
    return render (request,'index.html',{'adresses':adresses})

def crepes_sucrees( request):
    return render (request,'crepes sucrées.html')

def crepes_salees(request):
    return render (request,'crepes salées.html')

def cheescake(request):
    return render(request, 'cheescake.html' )

def commande(request):
    sucree=menu.objects.filter(cat_id=2)
    salee=menu.objects.filter(cat_id=1)
    cheese=menu.objects.filter(cat_id=3)
    return render(request,'commande.html',{'sucree':sucree, 'salee':salee, 'cheese':cheese})

def cmd(request):
    if request.method=='POST':
        form1=menuu(request.POST).save()
        return redirect ('cmd/val')
    else:
        form1=menuu()
    return render (request,'cmd.html',{'form1':form1 })

def val(request):
    if request.method=='POST':
        form2=validation(request.POST).save()
        return redirect('cmd')
    else:
        form2=validation()
    return render (request,'val.html',{'form2':form2})



    
"""class Films:
    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
    
movies=[Films('hunger game','Suzanne Collins','science fiction' ),Films('It','	Andy Muschietti','horror'),Films('bird box','Susanne Bier','thriller')]
"""