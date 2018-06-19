from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def api_404(request):
    raise NotFound()
