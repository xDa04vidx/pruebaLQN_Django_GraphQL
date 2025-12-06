import graphene
from .queries import Query
from .mutations.index import Mutation
from .models import *
schema = graphene.Schema(query=Query, mutation=Mutation)