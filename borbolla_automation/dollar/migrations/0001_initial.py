# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-06-02 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128, unique=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('ultima_modificacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compra', models.FloatField()),
                ('venta', models.FloatField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('ultima_modificacion', models.DateField(auto_now=True)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dollar.Banco')),
            ],
        ),
    ]