from typing import ItemsView
from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse_lazy
from django.views.generic import *


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
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Локация',
                                 blank=True,
                                 null=True,
                                 default=1,)

    information = models.TextField(verbose_name='Контактные данные',
                                   blank=True,
                                   null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'


class ClientCreate(CreateView):
    model = Client
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('client_list')

    def model_name(self):
        return self.model._meta.verbose_name


class ClientRead(DetailView):
    model = Client

    def model_name(self):
        return self.model._meta.verbose_name


class ClientUpdate(UpdateView):
    model = Client
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('client_list')

    def model_name(self):
        return self.model._meta.verbose_name


class ClientDelete(DeleteView):
    model = Client
    template_name = 'database/base_d_form.html'

    def get_success_url(self):
        return reverse_lazy('client_list')

    def model_name(self):
        return self.model._meta.verbose_name


class ClientList(ListView):
    model = Client

    def model_name(self):
        return self.model._meta.verbose_name
