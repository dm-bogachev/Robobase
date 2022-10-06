from django.db import models
from django.views.generic import *
from simple_history.models import HistoricalRecords


class RobotSeller(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    name = models.CharField(max_length=32,
                            unique=True,
                            verbose_name='Поставщик',)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Поставщики'
        verbose_name = 'Поставщик'
