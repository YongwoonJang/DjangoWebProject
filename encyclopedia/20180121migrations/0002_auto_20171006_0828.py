# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Content',
            new_name='ContentForDjango',
        ),
    ]
