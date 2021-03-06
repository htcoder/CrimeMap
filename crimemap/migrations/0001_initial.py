# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.IntegerField()),
                ('crime_date', models.DateTimeField(verbose_name='date published')),
                ('comp_name', models.CharField(max_length=200)),
                ('type_of_crime', models.CharField(max_length=200)),
                ('loc_lat', models.IntegerField()),
                ('loc_lon', models.IntegerField()),
                ('dec', models.CharField(max_length=500)),
            ],
        ),
    ]
