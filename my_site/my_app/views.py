from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from my_app.models import crepe, categorie, clients
from .formulaire import menuu, validation 
from django.urls import reverse


# Create your views here.

adresses=['Menzah5','Aouina']


def index(request):
    return render (request,'index.html',{'menu':menu, 'adresses':adresses})

def crepes_sucrees( request):
    return render (request,'crepes sucrées.html')

def crepes_salees(request):
    return render (request,'crepes salées.html')

def cheescake(request):
    return render(request, 'cheescake.html' )

def commande(request):
    sucree=crepe.objects.filter(cat_id=2)
    salee=crepe.objects.filter(cat_id=1)
    chees=crepe.objects.filter(cat_id=3)
    return render(request,'commande.html',{'sucree':sucree, 'salee':salee, 'chees':chees})

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

def menu(request):
    return render(request, 'menu.html' )

def contacts(request):
    return render(request, 'contacts.html' )

def pdv(request):
    return render (request, 'pdv.html')

def compte(request):
    if  request.user.is_authenticated :
        return HttpResponseRedirect (reverse("login"))
            
def login(request):
    return render(request, "login.html")

    
