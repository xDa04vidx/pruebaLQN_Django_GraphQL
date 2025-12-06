import graphene
from graphene_django import DjangoObjectType
from .models import *


class DirectorType(DjangoObjectType):
    peliculas = graphene.List(lambda: PeliculaType)

    class Meta:
        model = Director
        fields = (
            "id",
            "nombre",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
            "rel_peliculas"
        )

    def resolve_peliculas(root, info):
        return [rel.pelicula for rel in root.rel_peliculas.all()]

class PeliculaType(DjangoObjectType):
    planetas = graphene.List(lambda: PlanetaType)
    personajes = graphene.List(lambda: PersonajeType)
    directores = graphene.List(lambda: DirectorType)
    productores = graphene.List(lambda: ProductorType)

    class Meta:
        model = Pelicula
        fields = (
            "id",
            "titulo",
            "texto_apertura",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
            "rel_planetas",
            "rel_personajes",
            "rel_directores",
            "rel_productores",
        )

    def resolve_planetas(root, info):
        return [rel.planeta for rel in root.rel_planetas.all()]

    def resolve_personajes(root, info):
        return [rel.personaje for rel in root.rel_personajes.all()]

    def resolve_directores(root, info):
        return [rel.director for rel in root.rel_directores.all()]

    def resolve_productores(root, info):
        return [rel.productor for rel in root.rel_productores.all()]


class PersonajeType(DjangoObjectType):
    peliculas = graphene.List(lambda: PeliculaType)
    planeta = graphene.Field(lambda: PlanetaType)

    class Meta:
        model = Personaje
        fields = (
            "id",
            "nombre",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )

    def resolve_peliculas(root, info):
        return [rel.pelicula for rel in root.rel_peliculas.all()]

    def resolve_planeta(root, info):
        return getattr(root, "planeta", None)

class PlanetaType(DjangoObjectType):
    peliculas = graphene.List(lambda: PeliculaType)
    personajes = graphene.List(lambda: PersonajeType)

    class Meta:
        model = Planeta
        fields = (
            "id",
            "nombre",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )

    def resolve_peliculas(root, info):
        return [rel.pelicula for rel in root.rel_peliculas.all()]

    def resolve_personajes(root, info):
        return root.personajes.all()

class ProductorType(DjangoObjectType):
    peliculas = graphene.List(lambda: PeliculaType)

    class Meta:
        model = Productor
        fields = (
            "id",
            "nombre",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )

    def resolve_peliculas(root, info):
        return [rel.pelicula for rel in root.rel_peliculas.all()]

class PeliculaDirectorType(DjangoObjectType):
    class Meta:
        model = PeliculaDirector
        fields = (
            "id",
            "pelicula",
            "director",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )

class PeliculaPersonajeType(DjangoObjectType):
    class Meta:
        model = PeliculaPersonaje
        fields = (
            "id",
            "pelicula",
            "personaje",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )

class PeliculaPlanetaType(DjangoObjectType):
    class Meta:
        model = PeliculaPlaneta
        fields = (
            "id",
            "pelicula",
            "planeta",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )

class PeliculaProductorType(DjangoObjectType):
    class Meta:
        model = PeliculaProductor
        fields = (
            "id",
            "pelicula",
            "productor",
            "fecha_creacion",
            "usuario_creacion",
            "fecha_modificacion",
            "usuario_modificacion",
        )
