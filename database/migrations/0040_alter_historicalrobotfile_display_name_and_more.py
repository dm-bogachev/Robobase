# Generated by Django 4.0.4 on 2022-11-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0039_historicalrobot_seller_robot_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrobotfile',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отображаемое имя (по желанию)'),
        ),
        migrations.AlterField(
            model_name='robotfile',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отображаемое имя (по желанию)'),
        ),
    ]
