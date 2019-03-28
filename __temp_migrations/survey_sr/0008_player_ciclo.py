# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-28 02:21
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_sr', '0007_player_carrera_padres'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='ciclo',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'], [11, '11']], null=True, verbose_name='¿En qué ciclo de la carrera se encuentra?'),
        ),
    ]
