from django.db import models
from django.views.generic import *
from simple_history.models import HistoricalRecords


class Client(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    name = models.CharField(max_length=255,
                            verbose_name="Клиент",
                            unique=True,
                            db_index=True,)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    location = models.ForeignKey('Location',
                                 on_delete=models.SET_NULL,
                                 verbose_name='Локация',
                                 blank=True,
                                 null=True,)
                                 #default=1,) # default = Неизвестно

    information = models.TextField(verbose_name='Контактные данные',
                                   blank=True,
                                   null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент' 
