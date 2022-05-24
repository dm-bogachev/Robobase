import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import *
from simple_history.models import HistoricalRecords

class RobotService(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    name = models.CharField(max_length=255,
                            verbose_name='Название',)