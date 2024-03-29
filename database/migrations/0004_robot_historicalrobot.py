# Generated by Django 4.0.4 on 2022-05-19 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0003_robotarm_robotcontroller_historicalrobotcontroller_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Имя')),
                ('arm_sn', models.CharField(db_index=True, max_length=32, verbose_name='Серийный номер робота')),
                ('controller_sn', models.CharField(db_index=True, max_length=32, verbose_name='Серийный номер контроллера')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('shipping_date', models.DateField(blank=True, null=True, verbose_name='Дата поставки')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('deleted', models.BooleanField(db_index=True, default=False, verbose_name='Удалённый')),
                ('arm', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.robotarm', verbose_name='Модель робота')),
                ('client', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.client', verbose_name='Клиент')),
                ('controller', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.robotcontroller', verbose_name='Контроллер')),
                ('integrator', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.integrator', verbose_name='Интегратор')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.location', verbose_name='Текущее местоположение')),
            ],
            options={
                'verbose_name': 'Робот',
                'verbose_name_plural': 'Роботы',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRobot',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Имя')),
                ('arm_sn', models.CharField(db_index=True, max_length=32, verbose_name='Серийный номер робота')),
                ('controller_sn', models.CharField(db_index=True, max_length=32, verbose_name='Серийный номер контроллера')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('shipping_date', models.DateField(blank=True, null=True, verbose_name='Дата поставки')),
                ('creation_date', models.DateField(blank=True, editable=False, verbose_name='Дата создания')),
                ('deleted', models.BooleanField(db_index=True, default=False, verbose_name='Удалённый')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('arm', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.robotarm', verbose_name='Модель робота')),
                ('client', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.client', verbose_name='Клиент')),
                ('controller', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.robotcontroller', verbose_name='Контроллер')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('integrator', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.integrator', verbose_name='Интегратор')),
                ('location', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.location', verbose_name='Текущее местоположение')),
            ],
            options={
                'verbose_name': 'historical Робот',
                'verbose_name_plural': 'historical Роботы',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
