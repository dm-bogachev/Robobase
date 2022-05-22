from django.utils.decorators import classonlymethod
from typing import ItemsView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import *
from simple_history.models import HistoricalRecords


class Robot(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Имя',
                            db_index=True,)

    arm_sn = models.CharField(max_length=32,
                              verbose_name='Серийный номер робота',
                              db_index=True,)

    controller_sn = models.CharField(max_length=32,
                                     verbose_name='Серийный номер контроллера',
                                     db_index=True,)

    description = models.TextField(verbose_name='Комментарий',
                                   blank=True,
                                   null=True,)

    shipping_date = models.DateField(null=True,
                                     blank=True,
                                     verbose_name='Дата поставки', )

    creation_date = models.DateField(auto_now=True,
                                     verbose_name='Дата создания',)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    controller = models.ForeignKey('RobotController',
                                   on_delete=models.SET_DEFAULT,
                                   verbose_name='Контроллер',
                                   default=1,)  # default = 'Неизвестно'

    arm = models.ForeignKey('RobotArm',
                            on_delete=models.SET_DEFAULT,
                            verbose_name='Модель робота',
                            default=1,)  # default = 'Неизвестно'

    client = models.ForeignKey('Client',
                               on_delete=models.SET_DEFAULT,
                               verbose_name='Клиент',
                               blank=True,
                               null=True,
                               default=1,)  # default = 'Неизвестно'

    integrator = models.ForeignKey('Integrator',
                                   on_delete=models.SET_DEFAULT,
                                   verbose_name='Интегратор',
                                   blank=True,
                                   null=True,
                                   default=1,)  # default = 'Неизвестно'

    location = models.ForeignKey('Location',
                                 on_delete=models.SET_NULL,
                                 verbose_name='Текущее местоположение',
                                 blank=True,
                                 null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Роботы'
        verbose_name = 'Робот'


class RobotCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Robot
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robot_list')


class RobotRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Robot


class RobotUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Robot
    template_name = 'database/base_cu_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robot_list')

    def model_name(self):
        return self.model._meta.verbose_name


class RobotDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Robot
    template_name = 'database/base_d_form.html'

    def dispatch(self, request, *args, **kwargs):
        pass
        i = 0
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('robot_list')

    def model_name(self):
        return self.model._meta.verbose_name


class RobotList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Robot

    def model_name(self):
        return self.model._meta.verbose_name
