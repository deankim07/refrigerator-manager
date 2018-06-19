"""refrigerator_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings

from core.views import api_404

from rest_framework_swagger.views import get_swagger_view

from items.views import VegetablesListCreateAPIView

schema_view = get_swagger_view(title='Refrigerator-manager API')


urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^rest-swagger/', schema_view),
    url(r'^vegetables/?$', VegetablesListCreateAPIView.as_view(), name='query_for_vegetables'),

    url(r'^.*', api_404, name='api_404'),
]
