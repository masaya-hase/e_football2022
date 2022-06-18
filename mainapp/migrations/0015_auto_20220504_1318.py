# Generated by Django 3.1.4 on 2022-05-04 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20220213_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='コンディションレベル')),
            ],
        ),
        migrations.CreateModel(
            name='InjuryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('injury_resistance_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='怪我耐性レベル')),
            ],
        ),
        migrations.CreateModel(
            name='ReverseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reverse_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='逆足レベル')),
            ],
        ),
        migrations.RemoveField(
            model_name='ability',
            name='condition_stability',
        ),
        migrations.RemoveField(
            model_name='ability',
            name='injury_resistance',
        ),
        migrations.RemoveField(
            model_name='ability',
            name='reverse_foot_accuracy',
        ),
        migrations.RemoveField(
            model_name='ability',
            name='reverse_foot_frequency',
        ),
        migrations.RemoveField(
            model_name='clubcategory',
            name='league_group',
        ),
        migrations.CreateModel(
            name='PlayerFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='accuracy_item', to='mainapp.reversecategory', verbose_name='逆足精度')),
                ('condition_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.conditioncategory', verbose_name='コンディションの波')),
                ('frequency_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='frequency_item', to='mainapp.reversecategory', verbose_name='逆足頻度')),
                ('injury_resistance_choice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainapp.injurycategory', verbose_name='怪我耐性')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.player', verbose_name='紐づき選手')),
            ],
        ),
    ]
