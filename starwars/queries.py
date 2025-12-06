import graphene
from graphene_django import DjangoObjectType
from .types import *
from .models import *

class Query(graphene.ObjectType):
    all_peliculas = graphene.List(PeliculaType)
    all_directores = graphene.List(DirectorType)
    all_planetas = graphene.List(PlanetaType)
    all_personajes = graphene.List(PersonajeType,nombre=graphene.String())
    all_productores = graphene.List(ProductorType)

    pelicula_by_title = graphene.Field(PeliculaType, titulo=graphene.String(required=True))
    director_by_name = graphene.Field(DirectorType, nombre=graphene.String(required=True))
    planeta_by_name = graphene.Field(PlanetaType, nombre=graphene.String(required=True))
    personaje_by_name = graphene.Field(PersonajeType, nombre=graphene.String(required=True))
    productor_by_name = graphene.Field(ProductorType, nombre=graphene.String(required=True))


    def resolve_all_peliculas(root, info):
        return Pelicula.objects.prefetch_related(
            'rel_directores__director',
            'rel_planetas__planeta',
            'rel_productores__productor',
            'rel_personajes__personaje'
        ).all()

    def resolve_all_directores(root, info):
        return Director.objects.prefetch_related('rel_peliculas__pelicula').all()

    def resolve_all_planetas(root, info):
        return Planeta.objects.prefetch_related('rel_peliculas__pelicula', 'personajes').all()

    def resolve_all_personajes(root, info, nombre=None):
        qs = Personaje.objects.select_related('planeta').prefetch_related('rel_peliculas__pelicula')
        if nombre:
            qs = qs.filter(nombre__icontains=nombre)
        return qs
    def resolve_all_productores(root, info):
        return Productor.objects.prefetch_related('rel_peliculas__pelicula').all()

    def resolve_pelicula_by_title(root, info, titulo):
        try:
            return Pelicula.objects.get(titulo=titulo)
        except Pelicula.DoesNotExist:
            return None

    def resolve_director_by_name(root, info, nombre):
        try:
            return Director.objects.get(nombre=nombre)
        except Director.DoesNotExist:
            return None

    def resolve_planeta_by_name(root, info, nombre):
        try:
            return Planeta.objects.get(nombre=nombre)
        except Planeta.DoesNotExist:
            return None

    def resolve_personaje_by_name(root, info, nombre):
        try:
            return Personaje.objects.get(nombre=nombre)
        except Personaje.DoesNotExist:
            return None

    def resolve_productor_by_name(root, info, nombre):
        try:
            return Productor.objects.get(nombre=nombre)
        except Productor.DoesNotExist:
            return None