from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"pages/index.html",{
        'title': 'Bienvenido'
    })

def sobre_nosotros(request):
    return render(request, "pages/sobre-nosotros.html",{
        "title":"Sobre nosotros"
    })
