# Generated by Django 2.1.1 on 2020-12-16 09:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20201216_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 9, 9, 32, 764625, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bidder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 9, 9, 32, 765204, tzinfo=utc)),
        ),
    ]
