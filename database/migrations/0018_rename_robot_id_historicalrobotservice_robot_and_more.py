# Generated by Django 4.0.4 on 2022-05-25 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_alter_historicalrobotservice_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalrobotservice',
            old_name='robot_id',
            new_name='robot',
        ),
        migrations.RenameField(
            model_name='robotservice',
            old_name='robot_id',
            new_name='robot',
        ),
    ]
