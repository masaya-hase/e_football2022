# Generated by Django 3.1.4 on 2022-01-26 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20220127_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='date_field',
        ),
    ]