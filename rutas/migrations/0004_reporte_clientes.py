# Generated by Django 2.0.3 on 2018-04-15 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20180404_1707'),
        ('rutas', '0003_auto_20180414_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='clientes',
            field=models.ManyToManyField(through='rutas.DeliveringOrder', to='crud.Cliente'),
        ),
    ]