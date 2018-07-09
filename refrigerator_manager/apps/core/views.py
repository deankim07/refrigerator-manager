from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound


@api_view(['GET', 'POST', 'PATCH', 'DELETE']) # pragma: no cover
def api_404(request):
    raise NotFound()


def tempo_view(request):  # pragma: no cover
    return render(request, 'index.html', {})
