# Generated by Django 3.1.4 on 2022-08-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_ability_defensive_consciousness'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=30, null=True, verbose_name='カラー')),
            ],
        ),
    ]
