from django.db import models
from django.conf import settings

from core.constant import PlaceConstant


class Place(models.Model):
    """
    DB table for place save item
    """
    name = models.CharField(max_length=20, choices=PlaceConstant.TYPE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
