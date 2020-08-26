from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    """title= "the hunger game"
    author="Suzanne Collins"
    context={'movie_name': title,"movie_author":author}"""
    return render (request,'index.html',{'movies':movies})

class Films:
    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
    
movies=[Films('hunger game','Suzanne Collins','science fiction' ),Films('It','	Andy Muschietti','horror'),Films('bird box','Susanne Bier','thriller')]
