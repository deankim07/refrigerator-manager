from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.authentication import SessionAuthentication

from items.models import Vegetables, Forks
from items.serializers import VegetablesSerializer, ForksSerializer


class VegetablesListCreateAPIView(ListCreateAPIView):
    """
    get:
        Get Vegetable List
    post:
        Create Vegetable Item
    """
    authentication_classes = (SessionAuthentication,)
    parser_classes = (JSONParser, MultiPartParser,)
    serializer_class = VegetablesSerializer
    queryset = Vegetables.objects.all()


class VegetableRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    get:
        Get Vegetable Item
    patch:
        Update Vegetable Item
    delete:
        delete Vegetable Item
    """
    authentication_classes = (SessionAuthentication,)
    parser_classes = (JSONParser, MultiPartParser,)
    serializer_class = VegetablesSerializer
    queryset = Vegetables.objects.all()
    lookup_url_kwarg = 'vegetable_id'


class ForksListCreateAPIView(ListCreateAPIView):
    """
        get:
            Get Fork List
        post:
            Create Fork Item
        """
    authentication_classes = (SessionAuthentication,)
    parser_classes = (JSONParser, MultiPartParser,)
    serializer_class = ForksSerializer
    queryset = Forks.objects.all()


class ForkRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
        get:
            Get Fork Item
        patch:
            Update Fork Item
        delete:
            delete Fork Item
        """
    authentication_classes = (SessionAuthentication,)
    parser_classes = (JSONParser, MultiPartParser,)
    serializer_class = ForksSerializer
    queryset = Forks.objects.all()
    lookup_url_kwarg = 'fork_id'

