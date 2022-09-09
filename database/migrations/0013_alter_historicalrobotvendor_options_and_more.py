# Generated by Django 4.0.4 on 2022-05-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_alter_historicalrobotarm_vendor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalrobotvendor',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Производитель', 'verbose_name_plural': 'historical Производители'},
        ),
        migrations.AlterModelOptions(
            name='robotvendor',
            options={'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
        migrations.AlterField(
            model_name='historicalrobotarm',
            name='vendor',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='database.robotvendor', verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='robotarm',
            name='name',
            field=models.CharField(db_index=True, max_length=32, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='robotarm',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='database.robotvendor', verbose_name='Производитель'),
        ),
        migrations.AlterUniqueTogether(
            name='robotarm',
            unique_together={('vendor', 'name')},
        ),
    ]
