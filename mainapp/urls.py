from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="inicio"),
    path('inicio/', views.index, name="index"),
    path('sobre-nosotros/', views.sobre_nosotros, name="sobre nosotros")
]
