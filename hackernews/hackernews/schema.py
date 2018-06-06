import graphene

import links.schema

# this Query automatically inherits the Query defined in links.schema
class Query(links.schema.Query, graphene.ObjectType):
    pass

# this Mutation works just like the Query in that it automatically inherits the Mutation from links.schema
class Mutation(links.schema.Mutation, graphene.ObjectType):
    pass

# this sets the global Schema values for the different types: Queries, Mutations, and Subscriptions
schema = graphene.Schema(query=Query, mutation=Mutation)