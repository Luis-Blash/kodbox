from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    descripcion = models.CharField(max_length=255,verbose_name="Descripcion")
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

class Noticias(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Titulo")
    subtitulo = models.CharField(max_length=250, verbose_name="Sub titulo")
    contenido = RichTextField(verbose_name="Contenido")
    imagen = models.ImageField(default="null",verbose_name="Imagen", upload_to="noticias")
    publico = models.BooleanField(verbose_name="¿Publico?")
    # Usuarios de Django
    usuario = models.ForeignKey(User, editable=False, verbose_name="Usuario", on_delete=models.CASCADE)
    # Muchas noticas, tienen muchas categorias
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorias", blank=True)
    creado_el = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    actualizado_el = models.DateTimeField(auto_now=True,verbose_name="Actualizado el")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        #ordering =  ['-creado_el']

    def __str__(self):
        return self.titulo
