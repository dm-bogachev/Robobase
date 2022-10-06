from django.db import models
from django.views.generic import *
from simple_history.models import HistoricalRecords


class Location(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    country = models.CharField(max_length=255,
                               verbose_name='Страна',)

    region = models.CharField(max_length=255,
                               verbose_name='Регион',
                               blank=True,
                               null=True,)

    city = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Город',)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    def __str__(self):
    	if self.region:
        	return self.country + "/" self.region + "/" + self.city
        else:
        	return self.country + "/" + self.city

    class Meta:
        verbose_name_plural = 'Локации'
        verbose_name = 'Локация'
