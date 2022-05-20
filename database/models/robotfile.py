import os

from database.models.robot import Robot
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

    robot = models.ForeignKey(to='Robot',
                              on_delete=models.CASCADE,
                              verbose_name='Относится к роботу',)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name_plural = 'Файлы робота'
        verbose_name = 'Файл робота'
