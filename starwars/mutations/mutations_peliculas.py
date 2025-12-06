import graphene
from ..types import PeliculaType
from ..models import Pelicula, Director, Planeta, Personaje, Productor

class CrearPelicula(graphene.Mutation):
    pelicula = graphene.Field(PeliculaType)
    ok = graphene.Boolean()

    class Arguments:
        titulo = graphene.String(required=True)
        texto_apertura = graphene.String()
        director_ids = graphene.List(graphene.Int)
        planeta_ids = graphene.List(graphene.Int)
        personaje_ids = graphene.List(graphene.Int)
        productor_ids = graphene.List(graphene.Int)

    def mutate(root, info, titulo, texto_apertura=None, director_ids=None, planeta_ids=None, personaje_ids=None, productor_ids=None):
        pelicula = Pelicula.objects.create(titulo=titulo, texto_apertura=texto_apertura)

        if director_ids:
            for d_id in director_ids:
                director = Director.objects.get(id=d_id)
                pelicula.rel_directores.create(director=director)
        if planeta_ids:
            for p_id in planeta_ids:
                planeta = Planeta.objects.get(id=p_id)
                pelicula.rel_planetas.create(planeta=planeta)
        if personaje_ids:
            for p_id in personaje_ids:
                personaje = Personaje.objects.get(id=p_id)
                pelicula.rel_personajes.create(personaje=personaje)
        if productor_ids:
            for p_id in productor_ids:
                productor = Productor.objects.get(id=p_id)
                pelicula.rel_productores.create(productor=productor)

        return CrearPelicula(pelicula=pelicula, ok=True)

# Agregar mas mutaciones, para editar o eliminar