# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydoct', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='State',
            field=models.IntegerField(default=0),
        ),
    ]
