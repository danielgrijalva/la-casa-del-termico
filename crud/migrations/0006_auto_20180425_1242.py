# Generated by Django 2.0.3 on 2018-04-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20180404_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chofer',
            name='correo',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='chofer',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]