# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-19 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181011_0051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('registro_invima', models.CharField(max_length=50)),
                ('expediente', models.TextField(max_length=1000)),
                ('consecutivo', models.CharField(blank=True, max_length=50, null=True)),
                ('observacion', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tnovedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('nombre', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='comentariofarmacia',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='farmacia',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='farmacia',
            name='horario_atencion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='farmacia',
            name='latitud',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farmacia',
            name='longitud',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farmacia',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='comentariofarmacia',
            name='calificacion',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='farmacia',
            name='nombre',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='farmacia',
            name='reputacion',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='novedad',
            name='farmacia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Farmacia'),
        ),
        migrations.AddField(
            model_name='novedad',
            name='tnovedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tnovedad'),
        ),
    ]
