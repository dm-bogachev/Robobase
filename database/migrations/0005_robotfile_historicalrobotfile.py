# Generated by Django 4.0.4 on 2022-05-19 10:10

import database.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0004_robot_historicalrobot'),
    ]

    operations = [
        migrations.CreateModel(
            name='RobotFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=255, verbose_name='Отображаемое имя')),
                ('file', models.FileField(upload_to=database.models.RobotFile.get_file_path, verbose_name='Файл')),
                ('type', models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла')),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.robot', verbose_name='Относится к роботу')),
            ],
            options={
                'verbose_name': 'Файл робота',
                'verbose_name_plural': 'Файлы робота',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRobotFile',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('display_name', models.CharField(max_length=255, verbose_name='Отображаемое имя')),
                ('file', models.TextField(max_length=100, verbose_name='Файл')),
                ('type', models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('robot', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.robot', verbose_name='Относится к роботу')),
            ],
            options={
                'verbose_name': 'historical Файл робота',
                'verbose_name_plural': 'historical Файлы робота',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
