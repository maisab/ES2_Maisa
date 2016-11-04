# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigoDaAmostra', models.IntegerField(default=0, verbose_name=b'Codigo da Amostra')),
                ('endereco', models.CharField(max_length=200, verbose_name=b'Endereco')),
                ('idade', models.IntegerField(default=0)),
                ('outros', models.CharField(max_length=200, verbose_name=b'Outros')),
                ('tipoDeDoacao', models.CharField(default=b'ES', max_length=2, choices=[(b'ES', b'Espontanea'), (b'CO', b'Convocada'), (b'RE', b'Reposicao'), (b'AU', b'Autologa')])),
                ('hospitalDeInternacao', models.CharField(max_length=200, verbose_name=b'Hospital de Internacao')),
                ('procedimento', models.CharField(default=b'CC', max_length=2, choices=[(b'CC', b'Coleta Convencional'), (b'AF', b'Aferese')])),
                ('data', models.DateTimeField(default=datetime.datetime.now, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name=b'Nome do Doador')),
                ('endereco', models.CharField(max_length=200, verbose_name=b'Endereco')),
                ('idade', models.IntegerField(default=0)),
                ('nomeDoPai', models.CharField(max_length=200, verbose_name=b'Nome do Pai')),
                ('nomeDoMae', models.CharField(max_length=200, verbose_name=b'Nome do Mae')),
                ('sexo', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('estadoCivil', models.CharField(default=b'S', max_length=1, choices=[(b'S', b'Solteiro'), (b'C', b'Casado'), (b'O', b'Outros')])),
                ('nacionalidade', models.CharField(max_length=200, verbose_name=b'Nacionalidade')),
                ('RG', models.CharField(max_length=15, verbose_name=b'RG')),
                ('orgaoExpedidor', models.CharField(max_length=10, verbose_name=b'Orgao Expedidor')),
                ('CPF', models.CharField(max_length=20, verbose_name=b'CPF')),
                ('profissao', models.CharField(max_length=100, verbose_name=b'Profissao')),
                ('trabalhoAtual', models.CharField(max_length=200, verbose_name=b'Trabalho Atual')),
                ('municipio', models.CharField(max_length=200, verbose_name=b'Municipio')),
                ('estado', models.CharField(max_length=200, verbose_name=b'Estado')),
                ('telefone', models.CharField(max_length=200, verbose_name=b'Telefone')),
                ('celular', models.CharField(max_length=200, verbose_name=b'celular')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name=b'Nome do Funcionario')),
                ('permissao', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name=b'Nome do Gerente')),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.IntegerField(default=0)),
                ('historico', models.CharField(max_length=1000)),
                ('votes', models.IntegerField(default=0)),
                ('doador', models.ForeignKey(to='hemonucleo.Doador')),
            ],
        ),
        migrations.CreateModel(
            name='UltimaDoacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('peso', models.CharField(max_length=10, verbose_name=b'Peso da amostra')),
                ('hematocrito', models.CharField(max_length=10, verbose_name=b'Hematocrito')),
                ('hemoglobina', models.CharField(max_length=10, verbose_name=b'Hemoglobina')),
                ('pulso', models.CharField(max_length=10, verbose_name=b'Pulso')),
                ('pressaoArterial', models.CharField(max_length=10, verbose_name=b'Pressao Arterial')),
                ('data', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('apto', models.CharField(default=b'IN', max_length=2, choices=[(b'AP', b'Apto'), (b'IN', b'Inapto'), (b'IT', b'Inapto Temporariamente')])),
                ('reacoes', models.CharField(default=b'GR', max_length=2, choices=[(b'NE', b'Nenhuma'), (b'LE', b'Leve'), (b'MO', b'Moderada'), (b'GR', b'Grave')])),
                ('descricaoDaReacao', models.CharField(max_length=200, verbose_name=b'Pulso')),
            ],
        ),
        migrations.AddField(
            model_name='doacao',
            name='doador',
            field=models.ForeignKey(to='hemonucleo.Doador'),
        ),
        migrations.AddField(
            model_name='doacao',
            name='funcionario',
            field=models.ForeignKey(to='hemonucleo.Funcionario'),
        ),
    ]
