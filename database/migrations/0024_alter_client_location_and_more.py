# Generated by Django 4.0.4 on 2022-09-08 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0023_alter_client_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.location', verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='location',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.location', verbose_name='Локация'),
        ),
    ]
