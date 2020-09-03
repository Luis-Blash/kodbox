from django.shortcuts import render, get_object_or_404
from blog.models import Noticias

# Create your views here.
def noticias(request):

    noticias_secundarias =  Noticias.objects.filter(publico=True).order_by("-creado_el")[1:]
    noticia_principal = Noticias.objects.filter(publico=True).order_by("-creado_el").first()

    return render(request,"noticias/lista_noticias.html",{
        "title":"Noticias",
        "noticia_principal":noticia_principal,
        "noticias_secundarias":noticias_secundarias
    })

# noticias separadas
def noticia(request, noticia_id):

    noticia = get_object_or_404(Noticias, id= noticia_id)

    return render(request, 'noticias/noticia-individual.html',{
        "noticia":noticia
    })