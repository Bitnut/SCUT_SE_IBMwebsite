# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0003_auto_20180224_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
