# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20160826_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(upload_to='static/images/subj_icons', verbose_name='Subject Icon'),
        ),
    ]
