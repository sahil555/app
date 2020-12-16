# Generated by Django 2.1.1 on 2020-12-16 09:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0004_auto_20201216_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 9, 14, 45, 740576, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bidder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 9, 14, 45, 740851, tzinfo=utc)),
        ),
    ]