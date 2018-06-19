from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.authentication import SessionAuthentication

from items.models import Vegetables
from items.serializers import VegetablesSerializer


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
