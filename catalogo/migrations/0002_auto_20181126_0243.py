# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-26 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='qtd_de_itens',
        ),
        migrations.AlterField(
            model_name='produto',
            name='altura',
            field=models.CharField(blank=True, db_column='altura', max_length=10, verbose_name='Altura(mts)'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='comprimento',
            field=models.CharField(blank=True, db_column='comprimento', max_length=10, verbose_name='Comprimento(mts)'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='largura',
            field=models.CharField(blank=True, db_column='largura', max_length=10, verbose_name='largura(mts)'),
        ),
    ]
