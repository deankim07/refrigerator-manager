# Generated by Django 2.0.4 on 2018-06-22 02:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
        ('items', '0002_vegetables_place'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vegetables',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forks',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place'),
        ),
        migrations.AddField(
            model_name='forks',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]