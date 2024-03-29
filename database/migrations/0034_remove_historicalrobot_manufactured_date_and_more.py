# Generated by Django 4.0.4 on 2022-10-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0033_alter_historicalrobot_controller_sn_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalrobot',
            name='manufactured_date',
        ),
        migrations.RemoveField(
            model_name='historicalrobot',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='manufactured_date',
        ),
        migrations.RemoveField(
            model_name='robot',
            name='seller',
        ),
        migrations.AlterField(
            model_name='historicalrobot',
            name='controller_sn',
            field=models.CharField(db_index=True, max_length=32, verbose_name='Серийный номер контроллера'),
        ),
        migrations.AlterField(
            model_name='historicalrobotfile',
            name='type',
            field=models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='controller_sn',
            field=models.CharField(db_index=True, max_length=32, verbose_name='Серийный номер контроллера'),
        ),
        migrations.AlterField(
            model_name='robotfile',
            name='type',
            field=models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла'),
        ),
    ]
