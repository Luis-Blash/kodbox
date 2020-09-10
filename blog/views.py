from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Noticias, Categoria

# Create your views here.


def noticias(request):

    noticias_secundarias = Noticias.objects.filter(publico=True).order_by("-creado_el")[1:]
    noticia_principal = Noticias.objects.filter(publico=True).order_by("-creado_el").first()
    # paginar noticias, que es cuantas mostrar
    paginacion = Paginator(noticias_secundarias, 2)
    # recoger numero de la pagina
    pagina = request.GET.get('page')
    pagina_noticia = paginacion.get_page(pagina)

    return render(request, "noticias/lista_noticias.html", {
        "title": "Noticias",
        "noticia_principal": noticia_principal,
        "noticias_secundarias": pagina_noticia
    })

# noticias separadas


def noticia(request, noticia_id):

    noticia = get_object_or_404(Noticias, id=noticia_id)

    return render(request, 'noticias/noticia-individual.html', {
        "noticia": noticia
    })

# por categoria


def categorias(request, categoria_id):

    categorias_individual = get_object_or_404(Categoria, id=categoria_id)

    noticia_principal = Noticias.objects.filter(publico=True, categorias=categoria_id).order_by("-creado_el").first()
    noticias_secundarias = Noticias.objects.filter(publico=True, categorias=categoria_id).order_by("-creado_el")[1:]

    # Paginacion
    paginacion = Paginator(noticias_secundarias, 2)
    pagina = request.GET.get('page')
    pagina_noticia = paginacion.get_page(pagina)

    return render(request, "categorias/categorias-indivudual.html", {
        "categoria": categorias_individual,
        "noticia_principal": noticia_principal,
        "noticias_secundarias": pagina_noticia
    })

# buscar noticia


def buscar_noticia(request):

    if request.method == 'POST':
        titulo = request.POST['titulo']

        noticas_busqueda = Noticias.objects.filter(titulo__contains=titulo,publico=True).order_by("-creado_el")
    
    return render(request, "noticias/noticias-buscadas.html", {
        "title": "Resultados",
        "noticas_busquedas": noticas_busqueda
    })
