import graphene

import links.schema

# this Query automatically inherits the Query defined in links.schema
class Query(links.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)