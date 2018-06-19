from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.conf import settings

from place.models import Place
from core.constant import VegetableConstant


class Vegetables(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=VegetableConstant.TYPE, null=True)
    save_begin = models.DateField(auto_now_add=True)
    storage_period = models.IntegerField(default=7)
    quantity = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        verbose_name_plural = 'vegetables'
        db_table = 'vegetable'

    @property
    def left_storage_period(self):
        days = timedelta(days=float(str(self.storage_period)))
        dead_line = self.save_begin + days
        left_days = dead_line - timezone.now().date()
        return left_days





