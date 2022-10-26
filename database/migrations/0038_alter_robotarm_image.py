# Generated by Django 4.0.4 on 2022-10-26 13:12

import database.models.RobotArm
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0037_alter_historicalrobot_manufactured_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robotarm',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=database.models.RobotArm.get_file_path, verbose_name='Изображение'),
        ),
    ]