# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydoct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('EMail', models.EmailField(max_length=30)),
                ('RandomCode', models.CharField(max_length=20)),
                ('AcivityCode', models.CharField(max_length=20)),
            ],
        ),
    ]
