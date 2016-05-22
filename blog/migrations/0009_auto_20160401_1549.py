# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-01 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160320_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='category',
            new_name='categoryA',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='frozen',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='salty',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='sweet',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='vegetarian',
        ),
        migrations.AddField(
            model_name='dish',
            name='categoryB',
            field=models.IntegerField(default=0),
        ),
    ]