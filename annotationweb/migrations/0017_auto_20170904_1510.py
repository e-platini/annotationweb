# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-09-04 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotationweb', '0016_auto_20170904_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processedimage',
            old_name='drop',
            new_name='rejected',
        ),
    ]
