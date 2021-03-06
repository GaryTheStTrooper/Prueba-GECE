# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-08 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.currency
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('amount_offered', otree.db.models.CurrencyField(choices=[(otree.currency.Currency('0'), otree.currency.Currency('0')), (otree.currency.Currency('1'), otree.currency.Currency('1')), (otree.currency.Currency('2'), otree.currency.Currency('2')), (otree.currency.Currency('3'), otree.currency.Currency('3')), (otree.currency.Currency('4'), otree.currency.Currency('4')), (otree.currency.Currency('5'), otree.currency.Currency('5')), (otree.currency.Currency('6'), otree.currency.Currency('6')), (otree.currency.Currency('7'), otree.currency.Currency('7')), (otree.currency.Currency('8'), otree.currency.Currency('8')), (otree.currency.Currency('9'), otree.currency.Currency('9')), (otree.currency.Currency('10'), otree.currency.Currency('10')), (otree.currency.Currency('11'), otree.currency.Currency('11')), (otree.currency.Currency('12'), otree.currency.Currency('12')), (otree.currency.Currency('13'), otree.currency.Currency('13')), (otree.currency.Currency('14'), otree.currency.Currency('14')), (otree.currency.Currency('15'), otree.currency.Currency('15')), (otree.currency.Currency('16'), otree.currency.Currency('16')), (otree.currency.Currency('17'), otree.currency.Currency('17')), (otree.currency.Currency('18'), otree.currency.Currency('18')), (otree.currency.Currency('19'), otree.currency.Currency('19')), (otree.currency.Currency('20'), otree.currency.Currency('20'))], null=True)),
                ('offer_accepted', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ultimatum_group', to='otree.Session')),
            ],
            options={
                'db_table': 'ultimatum_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('round_payoff', otree.db.models.FloatField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ultimatum.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ultimatum_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ultimatum_player', to='otree.Session')),
            ],
            options={
                'db_table': 'ultimatum_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ultimatum_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'ultimatum_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatum.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ultimatum.Subsession'),
        ),
    ]
