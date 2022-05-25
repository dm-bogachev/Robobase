import os

from django.utils import timezone
from database.models.robot import Robot
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import *
from simple_history.models import HistoricalRecords


class RobotFile(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    TYPES = (
        ('photo', 'Фотография'),
        ('backup', 'Резервная копия'),
        ('other', 'Другое'),
        ('docs', 'Документы'),)

    def get_file_path(instance, filename):
        from random import randint
        from sys import maxsize
        robot = Robot.objects.get(pk=instance.robot_id)
        folder = [str(instance.robot_id), robot.name,
                  robot.arm_sn, robot.controller_sn]
        fname = [str(instance.display_name), str(
            randint(0, maxsize)), filename]
        return os.path.join('robots',
                            # Robot id + robot name + randint
                            '_'.join(folder),
                            # File type (photo, backup, other)
                            str(instance.type),
                            # Display name + randint + filename
                            '_'.join(fname),)

    display_name = models.CharField(max_length=255,
                                    verbose_name='Отображаемое имя',)

    file = models.FileField(verbose_name='Файл',
                            upload_to=get_file_path,)

    type = models.CharField(max_length=255,
                            choices=TYPES,
                            verbose_name='Тип файла',)

    upload_date = models.DateField(auto_now=True,
                                   verbose_name='Дата создания',)

    robot = models.ForeignKey(to='Robot',
                              on_delete=models.CASCADE,
                              verbose_name='Относится к роботу',)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name_plural = 'Файлы робота'
        verbose_name = 'Файл робота'


class RobotFileCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = RobotFile
    template_name = 'database/base_cu_form.html'
    fields = ['display_name', 'file', 'type']

    def form_valid(self, form):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        form.instance.robot = robot
        form.save()
        return super(RobotFileCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def model_name(self):
        return self.model._meta.verbose_name


class RobotFileDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = RobotFile
    template_name = 'database/base_d_form.html'
    
    def get_success_url(self):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(robotfile=pk)
        return reverse_lazy('robot_read', kwargs={'pk': robot.pk})

    def model_name(self):
        return self.model._meta.verbose_name