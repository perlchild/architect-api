# Generated by Django 2.0.1 on 2018-02-13 15:30

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('monitor', '0001_initial'), ('monitor', '0002_auto_20180202_1104'), ('monitor', '0003_auto_20180208_2121'), ('monitor', '0004_auto_20180213_1045')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='active', max_length=32)),
                ('engine', models.CharField(default='prometheus', max_length=32)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=511)),
                ('name', models.CharField(max_length=511)),
                ('kind', models.CharField(max_length=32)),
                ('size', models.IntegerField(default=1)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='unknown', max_length=32)),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='monitor.Monitor')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
