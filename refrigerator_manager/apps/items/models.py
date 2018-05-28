from datetime import timedelta
from django.db import models
from django.utils import timezone

from place.models import Place
from core.constant import CategoryConstant


class Paprika(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CategoryConstant.TYPE,
                                default=CategoryConstant.VEGETABLE)
    save_begin = models.DateField(auto_now_add=True)
    storage_period = models.IntegerField(default=7)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'paprikas'
        db_table = 'paprika'

    @property
    def left_storage_period(self):
        days = timedelta(days=float(str(self.storage_period)))
        dead_line = self.save_begin.date() + days
        left_days = dead_line - timezone.now()
        return left_days



