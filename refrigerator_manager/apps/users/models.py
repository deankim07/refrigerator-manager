from django.db import models

from django.urls import reverse

from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):

    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    is_member = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})