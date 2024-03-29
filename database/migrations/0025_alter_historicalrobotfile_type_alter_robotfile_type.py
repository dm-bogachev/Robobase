# Generated by Django 4.0.4 on 2022-10-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0024_alter_client_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrobotfile',
            name='type',
            field=models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('report', 'Oтчет по работам'), ('check', 'Чек-лист'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла'),
        ),
        migrations.AlterField(
            model_name='robotfile',
            name='type',
            field=models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('report', 'Oтчет по работам'), ('check', 'Чек-лист'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла'),
        ),
    ]
