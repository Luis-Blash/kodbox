from blog.models import Categoria, Noticias

def get_categorias(request):
    # si estan en uso
    categorias_uso= Noticias.objects.filter(publico=True).values_list("categorias", flat=True)
    categorias = Categoria.objects.filter(id__in=categorias_uso).values_list("id","nombre")

    return {
        "categorias": categorias,
        "id": categorias_uso
    }