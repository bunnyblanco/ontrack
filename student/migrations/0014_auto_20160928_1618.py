# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-28 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20160926_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
