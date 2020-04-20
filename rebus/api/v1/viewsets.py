from rest_framework import authentication
from rebus.models import Categorie, Lettrebus
from .serializers import CategorieSerializer, LettrebusSerializer
from rest_framework import viewsets


class CategorieViewSet(viewsets.ModelViewSet):
    serializer_class = CategorieSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Categorie.objects.all()


class LettrebusViewSet(viewsets.ModelViewSet):
    serializer_class = LettrebusSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Lettrebus.objects.all()
