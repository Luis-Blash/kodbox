from django.urls import path
from . import views


urlpatterns = [
    path("noticias/", views.noticias, name="noticias"),
    path("noticia/<int:noticia_id>", views.noticia, name="noticia"),
    path("categorias/<int:categoria_id>", views.categorias, name="categoria")
]
