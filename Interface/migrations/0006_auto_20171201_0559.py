# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0005_landmark_order_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huntuser',
            name='current_landmark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Interface.Landmark'),
        ),
    ]
