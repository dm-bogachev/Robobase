from typing import ItemsView
from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse_lazy
from django.views.generic import *


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


class RobotDetail(DetailView):
    model = Robot

class RobotList(ListView):
    model = Robot

class RobotCreate(CreateView):
    model = Robot
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robot_list')
