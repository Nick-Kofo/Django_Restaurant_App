# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-12 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
