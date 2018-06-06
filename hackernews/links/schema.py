import graphene
from graphene_django import DjangoObjectType

from .models import Link

# this declares 'Link' as a special type of data (will be stored as "Links" in the database)
class LinkType(DjangoObjectType):
    class Meta:
        # sets the value of the Link Type equal to the Link Model
        model = Link

# defines the Query for the Link Type
class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    # the resolver function returns all the Links that have been created and stored
    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

# this creates the mutation named 'CreateLink' that will allow you to add new Links to the database
class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    # this actually creates the link on the database
    def mutate(self, info, url, description):
        link = Link(url=url, description=description)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description
        )

# this is the actual mutation class, the Query class. It calls the CreateLink class to create a new Link
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()