# Generated by Django 3.1.4 on 2022-01-26 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20211230_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='new_date_field',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 26, 15, 10, 30, 858692, tzinfo=utc), null=True, verbose_name='リリース日'),
        ),
    ]
