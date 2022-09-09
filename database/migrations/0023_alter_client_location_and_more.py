# Generated by Django 4.0.4 on 2022-09-08 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0022_alter_client_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='location',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.location', verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='historicalclient',
            name='location',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.location', verbose_name='Локация'),
        ),
    ]
