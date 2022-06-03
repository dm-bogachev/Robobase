from django.db import models
from django.views.generic import *
from simple_history.models import HistoricalRecords


class Location(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    country = models.CharField(max_length=255,
                               verbose_name='Страна',)

    city = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Город',)

    def __str__(self):
        return self.country + "/" + self.city

    class Meta:
        verbose_name_plural = 'Локации'
        verbose_name = 'Локация'
