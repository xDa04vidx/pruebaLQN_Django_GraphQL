import graphene
from ..types import PersonajeType
from ..models import Personaje, Planeta

class CrearPersonaje(graphene.Mutation):
    personaje = graphene.Field(PersonajeType)
    ok = graphene.Boolean()

    class Arguments:
        nombre = graphene.String(required=True)
        planeta_id = graphene.Int()

    def mutate(root, info, nombre, planeta_id=None):
        planeta = None
        if planeta_id:
            planeta = Planeta.objects.get(id=planeta_id)
        personaje = Personaje.objects.create(nombre=nombre, planeta=planeta)
        return CrearPersonaje(personaje=personaje, ok=True)

# Agregar mas mutaciones, para editar o eliminar