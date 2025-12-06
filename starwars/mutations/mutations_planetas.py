import graphene
from ..types import PlanetaType
from ..models import Planeta

class CrearPlaneta(graphene.Mutation):
    planeta = graphene.Field(PlanetaType)
    ok = graphene.Boolean()

    class Arguments:
        nombre = graphene.String(required=True)

    def mutate(root, info, nombre):
        planeta = Planeta.objects.create(nombre=nombre)
        return CrearPlaneta(planeta=planeta, ok=True)
    
# Agregar mas mutaciones, para editar o eliminar