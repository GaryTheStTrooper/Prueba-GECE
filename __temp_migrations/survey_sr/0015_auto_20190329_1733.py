# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-29 22:33
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_sr', '0014_player_preg1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='preg1',
        ),
        migrations.AddField(
            model_name='player',
            name='preg11',
            field=otree.db.models.StringField(choices=[('Si', 'Si'), ('No', 'No')], max_length=10000, null=True, verbose_name=''),
        ),
    ]
