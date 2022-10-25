import datetime

from django.db import models
from django.views.generic import *
from simple_history.models import HistoricalRecords


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

    deleted = models.BooleanField(default=False,
                                  verbose_name='Удалённый',
                                  db_index=True,)

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
