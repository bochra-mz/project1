from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
menu= ['crepes sucrées','crepes salées','cheescake']
adresses=['Menzah5','Aouina']


def index(request):
    return render (request,'index.html',{'menu':menu, 'adresses':adresses})

def crepe_sucree( request):
    return render (request,'crepe_sucre.html')

"""class Films:
    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
    
movies=[Films('hunger game','Suzanne Collins','science fiction' ),Films('It','	Andy Muschietti','horror'),Films('bird box','Susanne Bier','thriller')]
"""