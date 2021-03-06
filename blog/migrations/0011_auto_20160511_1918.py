# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-11 16:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160418_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='author',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dish',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/'),
        ),
    ]
