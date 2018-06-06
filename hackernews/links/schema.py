import graphene
from graphene_django import DjangoObjectType

from .models import Link


# a special instance of type created with DjangoObjectType
class LinkType(DjangoObjectType):
    class Meta:
        model = Link


# the Query Type that returns all the links
class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    # the resolver function
    def resolve_links(self, info, **kwargs):
        return Link.objects.all()