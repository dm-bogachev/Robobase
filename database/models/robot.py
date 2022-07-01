from django.conf import settings
from django.db import models
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
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Текущее местоположение',
                                 blank=True,
                                 null=True,
                                 default=1,) # default = 'Неизвестно'

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_DEFAULT,
                                 verbose_name='Кем добавлен',
                                 default=1,)

    def __str__(self):
        return self.name
    
    # def save(self, request, *args, **kwargs) -> None:
    #     self.added_by = request.user
    #     return super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Роботы'
        verbose_name = 'Робот'
