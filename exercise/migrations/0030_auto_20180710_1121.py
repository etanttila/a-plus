# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-10 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0029_ltiexercise_open_in_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltiexercise',
            name='resource_link_title',
            field=models.CharField(blank=True, help_text='Default: the menu label of the LTI service', max_length=128),
        ),
    ]