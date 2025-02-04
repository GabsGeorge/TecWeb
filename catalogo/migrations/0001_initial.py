# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-26 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now_add=True, verbose_name='modificado em')),
                ('imagem', models.ImageField(blank=True, db_column='Imagem', null=True, upload_to='media')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
                'ordering': ['nome'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_f', models.CharField(db_column='Nome_F', max_length=100, unique=True, verbose_name='Nome')),
                ('email_f', models.CharField(blank=True, db_column='Email_F', max_length=100, null=True, verbose_name='Email')),
                ('endereco_f', models.CharField(db_column='Endereco_F', max_length=255, verbose_name='Endereco')),
                ('telefoneprincipal', models.IntegerField(db_column='TelefonePrincipal', verbose_name='Telefone principal')),
                ('telefonesecundario', models.IntegerField(blank=True, db_column='TelefoneSecundario', null=True, verbose_name='Telefone Secundário')),
                ('categoria_f', models.CharField(db_column='Categoria_F', max_length=100, verbose_name='Categoria de produtos')),
            ],
            options={
                'db_table': 'Fornecedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo_p', models.AutoField(db_column='Codigo_P', primary_key=True, serialize=False, verbose_name='código produto')),
                ('nome_p', models.CharField(db_column='Nome_P', max_length=100, verbose_name='Nome do produto')),
                ('quantidade', models.SmallIntegerField(db_column='Quantidade', verbose_name='Quantidade')),
                ('imagem', models.ImageField(db_column='Imagem', upload_to='media', verbose_name='Imagem')),
                ('descricao', models.TextField(db_column='Descricao_P', verbose_name='Descrição')),
                ('custo_p', models.DecimalField(db_column='Custo_P', decimal_places=2, max_digits=10, verbose_name='Custo')),
                ('preco_p', models.DecimalField(db_column='Preço_P', decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('altura', models.CharField(db_column='altura', max_length=10, verbose_name='Altura(mts)')),
                ('largura', models.CharField(db_column='largura', max_length=10, verbose_name='largura(mts)')),
                ('comprimento', models.CharField(db_column='comprimento', max_length=10, verbose_name='Comprimento(mts)')),
                ('peso', models.DecimalField(db_column='peso', decimal_places=4, max_digits=10, verbose_name='Peso(kg)')),
                ('qtd_de_itens', models.SmallIntegerField(db_column='Quantidade de Itens', verbose_name='Quantidade de itens do kit')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('vender', models.BooleanField(db_column='Vender', default=True)),
                ('ativo', models.BooleanField(db_column='Ativo', default=True)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now_add=True, verbose_name='modificado em')),
                ('categoria_p', models.ForeignKey(db_column='categoria_p', on_delete=django.db.models.deletion.DO_NOTHING, to='catalogo.Categoria')),
                ('nome_f', models.ForeignKey(db_column='Nome Fornecedor', on_delete=django.db.models.deletion.DO_NOTHING, to='catalogo.Fornecedor')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'Produto',
                'ordering': ['nome_p'],
                'managed': True,
            },
        ),
    ]
