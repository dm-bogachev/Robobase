import os
from django.db import models
from simple_history.models import HistoricalRecords


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
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'


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


class RobotArm(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    def get_file_path(instance, filename):
        from random import randint
        from sys import maxsize
        fname = [str(instance.name), str(randint(0, maxsize)), filename]
        return os.path.join('arm_images',
                            '_'.join(fname),)

    name = models.CharField(max_length=32,
                            unique=True,
                            verbose_name='Модель',
                            db_index=True,)

    image = models.ImageField(upload_to=get_file_path,
                              null=True,
                              blank=True,)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Модели'
        verbose_name = 'Модель'


class RobotController(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    def get_file_path(instance, filename):
        from random import randint
        from sys import maxsize
        fname = [str(instance.name), str(randint(0, maxsize)), filename]
        return os.path.join('controller_images',
                            '_'.join(fname),)

    name = models.CharField(max_length=32,
                            unique=True,
                            verbose_name='Контроллер',
                            db_index=True,)

    image = models.ImageField(upload_to=get_file_path,
                              null=True,
                              blank=True,)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Контроллеры'
        verbose_name = 'Контроллер'


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
