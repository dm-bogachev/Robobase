import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import *
from simple_history.models import HistoricalRecords


class RobotVendor(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    name = models.CharField(max_length=32,
                            unique=True,
                            verbose_name='Производитель',)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Производители'
        verbose_name = 'Производитель'