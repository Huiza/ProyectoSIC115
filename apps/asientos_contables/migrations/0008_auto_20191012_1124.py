# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2019-10-12 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asientos_contables', '0007_auto_20191011_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librodiario',
            name='asientoD',
        ),
        migrations.DeleteModel(
            name='libroDiario',
        ),
    ]
