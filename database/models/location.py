from typing import ItemsView
from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse_lazy
from django.views.generic import *


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


class LocationCreate(CreateView):
    model = Location
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('location_list')

    def model_name(self):
        return self.model._meta.verbose_name


class LocationRead(DetailView):
    model = Location

    def model_name(self):
        return self.model._meta.verbose_name


class LocationUpdate(UpdateView):
    model = Location
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('location_list')

    def model_name(self):
        return self.model._meta.verbose_name


class LocationDelete(DeleteView):
    model = Location
    template_name = 'database/base_d_form.html'

    def get_success_url(self):
        return reverse_lazy('location_list')

    def model_name(self):
        return self.model._meta.verbose_name


class LocationList(ListView):
    model = Location

    def model_name(self):
        return self.model._meta.verbose_name
