# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160106_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='developer',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
