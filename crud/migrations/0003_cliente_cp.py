# Generated by Django 2.0.3 on 2018-04-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20180323_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]