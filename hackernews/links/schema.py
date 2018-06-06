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