# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0004_auto_20180303_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
