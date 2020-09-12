# kodbox

Un proyecto de practica usando Django, para la creacion de una web de noticias, usuando como ejemplo [KODBOX](https://www.youtube.com/channel/UCoEIYAsPco1b1AKyDDVi3fg), una canl creado para la enseñanza en programación y tecnologia.

Primero para empezar necesitamos instalar lo que necesitamos
```	
pip install -r requirements.txt
```

Una vez instalado vamos a ir a manage.py, el cual vamos a hacer la migracion y un super usuario

```python
python3 manage.py migrate
python3 manage.py createsuperuser

```
y para terminar vamos a correr el servidor

```python

python manage.py runserver

```

## Inico y sobre nosotros
Primero que nada da la bienvenida a la pagina principal
![Inicio](https://github.com/Luis-Blash/kodbox/tree/master/github/Bienvenida.png)

<hr>

![Sobre](https://github.com/Luis-Blash/kodbox/tree/master/github/sobre.png)

## Noticias
En la pagina de ***Noticias*** tenemos la muestra del titulo, subtitulo, imagen y el dia de creacion, con el boton de ir.
Se divide en Noticia principal, noticias secuandarios
![bienvenida](https://github.com/Luis-Blash/kodbox/tree/master/github/noticias.png)

### Noticias Individual
Cada noticia te lleva a su contenido
![Noticia Individual](https://github.com/Luis-Blash/kodbox/tree/master/github/noticiaIndividual.png)

### Categorias
Usando las categorias de cada una de las Noticias, puede llevarte a la lista de solo las noticias por categorias.
![Por categoria](https://github.com/Luis-Blash/kodbox/tree/master/github/porCategorias.png)

### Busquedas
La busqueda funciona por un metodo post, la cual busca todas las noticias publicas y que en su nombre venga esa palabra
![Por categoria](https://github.com/Luis-Blash/kodbox/tree/master/github/porBusqueda.png)
