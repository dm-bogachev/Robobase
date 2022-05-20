from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse_lazy
from django.views.generic import *


class Integrator(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    name = models.CharField(max_length=255,
                            verbose_name="Интегратор",
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

    information = models.TextField(verbose_name='Контактные данные',
                                   blank=True,
                                   null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Интеграторы'
        verbose_name = 'Интеграторы'


class IntegratorCreate(CreateView):
    model = Integrator
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('integrator_list')

    def model_name(self):
        return self.model._meta.verbose_name


class IntegratorRead(DetailView):
    model = Integrator

    def model_name(self):
        return self.model._meta.verbose_name


class IntegratorUpdate(UpdateView):
    model = Integrator
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('integrator_list')

    def model_name(self):
        return self.model._meta.verbose_name


class IntegratorDelete(DeleteView):
    model = Integrator
    template_name = 'database/base_d_form.html'

    def get_success_url(self):
        return reverse_lazy('integrator_list')

    def model_name(self):
        return self.model._meta.verbose_name


class IntegratorList(ListView):
    model = Integrator

    def model_name(self):
        return self.model._meta.verbose_name
