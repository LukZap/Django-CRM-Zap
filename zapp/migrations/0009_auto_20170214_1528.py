# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapp', '0008_auto_20170214_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_assistant',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer_assistant',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]