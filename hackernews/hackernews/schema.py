import graphene
import graphql_jwt

import links.schema
import users.schema

# this Query automatically inherits the Query defined in links.schema
class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

# this Mutation works just like the Query in that it automatically inherits the Mutation from links.schema
# it also sets the variables for holding the JWT for authentication
class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

# this sets the global Schema values for the different types: Queries, Mutations, and Subscriptions
schema = graphene.Schema(query=Query, mutation=Mutation)