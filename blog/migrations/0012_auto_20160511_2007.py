# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-11 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160511_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to=settings.AUTH_USER_MODEL),
        ),
    ]
