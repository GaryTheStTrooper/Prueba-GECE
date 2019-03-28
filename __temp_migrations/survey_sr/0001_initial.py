# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-03-28 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0002_session_mturk_expiration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_sr_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_sr_group',
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
                ('question_id', otree.db.models.PositiveIntegerField(null=True)),
                ('question', otree.db.models.StringField(max_length=10000, null=True)),
                ('submitted_answer', otree.db.models.StringField(max_length=10000, null=True)),
                ('age', otree.db.models.PositiveIntegerField(null=True, verbose_name='¿Cuál es tu edad?')),
                ('gender', otree.db.models.StringField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=10000, null=True, verbose_name='¿Cuál es tu género?')),
                ('provincia', otree.db.models.StringField(choices=[('Lima', 'Lima'), ('Callao', 'Callao'), ('Otro', 'Otro')], max_length=10000, null=True, verbose_name='¿Indique la provincia en la que reside?')),
                ('distrito', otree.db.models.PositiveIntegerField(choices=[[0, 'Callao'], [1, 'Ancón'], [2, 'Ate'], [3, 'Barranco'], [4, 'Breña'], [5, 'Carabayllo'], [6, 'Chaclacayo'], [7, 'Chorrillos'], [8, 'Cieneguilla'], [9, 'Comas'], [10, 'El Agustino'], [11, 'Independencia'], [12, 'Jesús María'], [13, 'La Molina'], [14, 'La Victoria'], [15, 'Lima'], [16, 'Lince'], [17, 'Los Olivos'], [18, 'Lurigancho'], [19, 'Lurín'], [20, 'Magdalena del Mar'], [21, 'Miraflores'], [22, 'Pachacamac'], [23, 'Pucusana'], [24, 'Pueblo Libre'], [25, 'Puente Piedra'], [26, 'Punta Hermosa'], [27, 'Punta Negra'], [28, 'Rímac'], [29, 'San Bartolo'], [30, 'San Borja'], [31, 'San Isidro'], [32, 'San Juan de Lurigancho'], [33, 'San Juan de Miraflores'], [34, 'San Luis'], [35, 'San Martín de Porres'], [36, 'San Miguel'], [37, 'Santa Anita'], [38, 'Santa María del Mar'], [39, 'Santa Rosa'], [40, 'Santiago de Surco'], [41, 'Surquillo'], [42, 'Villa El Salvador'], [43, 'Villa María del Triunfo'], [99, 'Otro / No Aplica']], null=True, verbose_name='¿Cuál es su distrito de residencia? (seleccione otro si su provincia de residencia no es Lima Metropolitana ni el Callao)')),
                ('field_studies', otree.db.models.PositiveIntegerField(choices=[[1, 'Administración de Negocios'], [2, 'Economía'], [3, 'Biología'], [4, 'Química'], [5, 'Ingeniería'], [6, 'Filisofía'], [7, 'Psicología'], [8, 'Física'], [9, 'Derecho'], [10, 'Historia'], [11, 'Lengua y Literatura Inglesa'], [12, 'Arqueología'], [13, 'Lengua y Literatura Alemana'], [14, 'Bioquímica'], [15, 'Bioinformática'], [16, 'Ciencias de la Nutrición'], [17, 'Ciencias de la Educación'], [18, 'Teología'], [19, 'Geografía'], [20, 'Lengua y Literatura Romana'], [21, 'Geología'], [22, 'Filología'], [23, 'Ciencias de la Computación'], [24, 'Tecnología de la información comercial'], [25, 'Lenguas Indo Germánicas'], [26, 'Historia del Arte'], [27, 'Matemáticas'], [28, 'Ciencia de los Medios'], [29, 'Musicología'], [30, 'Idiomas y Literatura Eslava'], [31, 'Farmacia'], [32, 'Ciencias Políticas'], [33, 'Sociología'], [34, 'Ciencias del Deporte'], [35, 'Prehistoria e Historia temprana'], [36, 'Odontología'], [37, 'Tecnología Médica'], [38, 'Antropología'], [99, 'Otro / No Aplica']], null=True, verbose_name='¿Cuál es su principal campo de estudios?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey_sr.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_sr_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_sr_player', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_sr_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_sr_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_sr_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_sr.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey_sr.Subsession'),
        ),
    ]
