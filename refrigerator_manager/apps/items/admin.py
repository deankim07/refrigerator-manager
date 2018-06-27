from django.contrib import admin

# Register your models here.
from .models import Vegetables, Forks


admin.site.register(Vegetables)
admin.site.register(Forks)

