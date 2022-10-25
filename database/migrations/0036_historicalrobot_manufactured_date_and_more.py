# Generated by Django 4.0.4 on 2022-10-25 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0035_historicalrobotfile_service_robotfile_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalrobot',
            name='manufactured_date',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='Дата производства'),
        ),
        migrations.AddField(
            model_name='robot',
            name='manufactured_date',
            field=models.DateField(auto_now=True, null=True, verbose_name='Дата производства'),
        ),
        migrations.AlterField(
            model_name='historicalrobotfile',
            name='service',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.robotservice', verbose_name='Относится к обслуживанию'),
        ),
        migrations.AlterField(
            model_name='historicalrobotfile',
            name='type',
            field=models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('report', 'Oтчет по работам'), ('check', 'Чек-лист'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла'),
        ),
        migrations.AlterField(
            model_name='robotfile',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.robotservice', verbose_name='Относится к обслуживанию'),
        ),
        migrations.AlterField(
            model_name='robotfile',
            name='type',
            field=models.CharField(choices=[('photo', 'Фотография'), ('backup', 'Резервная копия'), ('report', 'Oтчет по работам'), ('check', 'Чек-лист'), ('other', 'Другое'), ('docs', 'Документы')], max_length=255, verbose_name='Тип файла'),
        ),
    ]
