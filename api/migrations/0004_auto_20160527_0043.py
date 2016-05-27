# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_kit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('nombre',)},
        ),
        migrations.AddField(
            model_name='item',
            name='kit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Kit'),
        ),
    ]