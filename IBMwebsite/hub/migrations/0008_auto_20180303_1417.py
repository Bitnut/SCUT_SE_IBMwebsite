# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0007_auto_20180303_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lead_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hub.User', unique=True),
        ),
    ]
