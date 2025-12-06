import graphene
from .queries import Query
from .mutations.index import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)