import graphene
from .mutations_personajes import CrearPersonaje
from .mutations_planetas import CrearPlaneta
from .mutations_peliculas import CrearPelicula

class Mutation(graphene.ObjectType):
    crear_personaje = CrearPersonaje.Field()
    crear_planeta = CrearPlaneta.Field()
    crear_pelicula = CrearPelicula.Field()
