# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 17:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_developer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='application',
            new_name='applications',
        ),
    ]
