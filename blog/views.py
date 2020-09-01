from django.shortcuts import render
from blog.models import Noticias

# Create your views here.
def noticias(request):

    noticias =  Noticias.objects.all()

    return render(request,"noticias/lista_noticias.html",{
        "title":"Noticias",
        "noticias":noticias
    })