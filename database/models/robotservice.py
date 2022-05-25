import datetime
import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import *
from simple_history.models import HistoricalRecords

from database.models.robot import Robot


class RobotService(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    date = models.DateField(verbose_name='Дата',
                            default=datetime.date.today)

    description = models.TextField(verbose_name='Описание',
                                   default=" ")

    robot = models.ForeignKey('Robot',
                              on_delete=models.CASCADE,
                              verbose_name='Робот',)

    def __str__(self):
        return self.description

    @property
    def days_from_service(self):
        from datetime import datetime
        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(datetime.now().date()), date_format)
        b = datetime.strptime(str(self.date), date_format)
        delta = b - a
        if delta.days < 0:
            return str(-delta.days) + ' дней назад'
        else:
            return 'Запланировано на ' + str(self.date.strftime("%d.%m.%Y")) + ' (через ' + str(
                delta.days) + ' дня(ей))'

    class Meta:
        verbose_name_plural = 'Обслуживания робота'
        verbose_name = 'Обслуживание робота'


class RobotServiceCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotService
    template_name = 'database/base_cu_form.html'
    fields = ['date', 'description']

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        form.instance.robot = robot
        form.save()
        return super(RobotServiceCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def model_name(self):
        return self.model._meta.verbose_name


class RobotServiceDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = RobotService
    template_name = 'database/base_d_form.html'

    def get_success_url(self):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(robotservice=pk)
        return reverse_lazy('robot_read', kwargs={'pk': robot.pk})

    def model_name(self):
        return self.model._meta.verbose_name
