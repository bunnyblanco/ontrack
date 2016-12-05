# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-02 18:16
from __future__ import unicode_literals

from django.db import migrations


##unsure about this, might just load from a csv file instead since I can't add to this one - 12/02/16

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    HighSchool = apps.get_model("student", "HighSchool")
    db_alias = schema_editor.connection.alias
    HighSchool.objects.using(db_alias).bulk_create([
        HighSchool(school_name="Walter Payton College Prep", short_name="Payton",
        school_type = "SES", admit_points=853, website="http://www.wpcp.org/")

    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates HS instances,
    # so reverse_func() should delete them.
    HighSchool = apps.get_model("student", "HighSchool")
    db_alias = schema_editor.connection.alias
    Country.objects.using(db_alias).filter(school_name="Walter Payton College Prep").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_auto_20161202_1758'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
