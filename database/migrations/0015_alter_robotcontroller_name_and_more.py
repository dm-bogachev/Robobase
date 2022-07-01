# Generated by Django 4.0.4 on 2022-05-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_historicalrobotcontroller_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robotcontroller',
            name='name',
            field=models.CharField(db_index=True, max_length=32, verbose_name='Контроллер'),
        ),
        migrations.AlterUniqueTogether(
            name='robotcontroller',
            unique_together={('vendor', 'name')},
        ),
    ]