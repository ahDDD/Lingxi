# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 04:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='belong_to',
            new_name='belong_to_answer',
        ),
    ]
