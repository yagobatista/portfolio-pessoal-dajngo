# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-09 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devnoob', '0006_auto_20171209_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='foto_perfil',
            field=models.ImageField(upload_to='perfil'),
        ),
    ]
