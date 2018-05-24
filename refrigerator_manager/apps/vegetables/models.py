from datetime import datetime, timedelta
from django.db import models

from place.models import Place
from core.constant import CategoryConstant


class Paprika(models.Model):

    place = models.ForeignKey(Place)
    category = models.CharField(max_length=20, choices=CategoryConstant.TYPE, default='Vegetable')
    save_begin = models.DateField(auto_now_add=True)
    storage_period = models.IntegerField(default=7)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'paprikas'
        db_table = 'paprika'

    @property
    def left_storage_period(self):
        days = timedelta(days=7)
        dead_line = self.save_begin - days
        left_days = dead_line - datetime.now()
        return left_days



