from django.db import models

from core.constant import PlaceConstant


class Place(models.Model):
    """
    DB table for place save item
    """
    name = models.CharField(max_length=20, choices=PlaceConstant.TYPE)
