import os
from django.db import models
from django.views.generic import *
from simple_history.models import HistoricalRecords


class RobotController(models.Model):
    # Historical records default model
    history = HistoricalRecords()

    def get_file_path(instance, filename):
        from random import randint
        from sys import maxsize
        fname = [str(instance.name), str(randint(0, maxsize)), filename]
        return os.path.join('controller_images',
                            '_'.join(fname),)

    vendor = models.ForeignKey('RobotVendor',
                               on_delete=models.SET_DEFAULT,
                               verbose_name='Производитель',
                               default=1,)  # default = 'Kawasaki'

    name = models.CharField(max_length=32,
                            verbose_name='Контроллер',
                            db_index=True,)

    image = models.FileField(upload_to=get_file_path,
                              null=True,
                              blank=True,)

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

    def __str__(self):
        return self.name + '/' + str(self.vendor)

    class Meta:
        verbose_name_plural = 'Контроллеры'
        verbose_name = 'Контроллер'
        unique_together = ('vendor', 'name',)
