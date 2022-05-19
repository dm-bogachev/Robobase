from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords


class Employee(AbstractUser):
    # Historical records default model
    history = HistoricalRecords(verbose_name='История изменений',)

    username = models.CharField(max_length=255,
                                unique=True,
                                verbose_name='Логин',)

    email = models.EmailField(unique=True,
                              null=False,
                              blank=True,
                              verbose_name='Эл. почта',)

    first_name = models.CharField(max_length=255,
                                  verbose_name='Имя',)

    last_name = models.CharField(max_length=255,
                                 verbose_name='Фамилия',
                                 db_index=True,)

    mid_name = models.CharField(max_length=255,
                                null=True,
                                blank=True,
                                verbose_name='Отчество',)

    birthday = models.DateField(null=True,
                                blank=True,
                                verbose_name='Дата рождения',)

    position = models.CharField(max_length=255,
                                null=True,
                                blank=True,
                                verbose_name='Должность',)

    # Model fields for the future use
    permission_service = models.BooleanField(verbose_name='Сервисный отдел',
                                             default=False,)

    permission_sales = models.BooleanField(verbose_name='Отдел продаж',
                                           default=False,)

    permission_accounting = models.BooleanField(verbose_name='Бухгалтерия',
                                                default=False,)

    permission_administration = models.BooleanField(verbose_name='Администратор',
                                                    default=False,)

    # Automatic assignment of administrator permission
    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.permission_administration = self.is_superuser
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name_plural = 'Сотрудники'
        verbose_name = 'Сотрудник'
