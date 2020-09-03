from django.contrib import admin
from .models import Categoria, Noticias
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado_el',)
    list_display = ("nombre","creado_el") 

class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ('usuario','creado_el','actualizado_el')
    search_fields = ("titulo","usuario__username","categorias__nombre")
    list_filter = ("publico","categorias__nombre","usuario__username")# filtros para escoger
    list_display = ("titulo","publico","creado_el") # para verlo con columnas

    # Cuand el editable esta a false, puede que no lo guarde
    # obtengo el objeto y que es de mi tabla, y le doy el id de la tabla user de django
    def save_model(self, request, obj, form, change):
        if not obj.usuario_id:
            obj.usuario_id = request.user.id
        
        obj.save()

# Registro
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticias, NoticiasAdmin)