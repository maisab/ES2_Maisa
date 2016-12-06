# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hemonucleo', '0002_doador_outrosdados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='endereco',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Endereco', blank=True),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='hospitalDeInternacao',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Hospital de Internacao', blank=True),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='idade',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='outros',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Outros', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='CPF',
            field=models.CharField(max_length=20, null=True, verbose_name=b'CPF', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='RG',
            field=models.CharField(max_length=15, null=True, verbose_name=b'RG', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='celular',
            field=models.CharField(max_length=200, null=True, verbose_name=b'celular', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='estado',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Estado', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='estadoCivil',
            field=models.CharField(default=b'S', max_length=1, null=True, blank=True, choices=[(b'S', b'Solteiro'), (b'C', b'Casado'), (b'O', b'Outros')]),
        ),
        migrations.AlterField(
            model_name='doador',
            name='municipio',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Municipio', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='nacionalidade',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Nacionalidade', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='nomeDoMae',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Nome do Mae', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='nomeDoPai',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Nome do Pai', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='orgaoExpedidor',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Orgao Expedidor', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='outrosDados',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Outros', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='profissao',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Profissao', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='telefone',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Telefone', blank=True),
        ),
        migrations.AlterField(
            model_name='doador',
            name='trabalhoAtual',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Trabalho Atual', blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='descricao',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='historico',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='votes',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='apto',
            field=models.CharField(default=b'IN', max_length=2, null=True, blank=True, choices=[(b'AP', b'Apto'), (b'IN', b'Inapto'), (b'IT', b'Inapto Temporariamente')]),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='hematocrito',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Hematocrito', blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='hemoglobina',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Hemoglobina', blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='peso',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Peso da amostra', blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='pressaoArterial',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Pressao Arterial', blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='pulso',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Pulso', blank=True),
        ),
        migrations.AlterField(
            model_name='ultimadoacao',
            name='reacoes',
            field=models.CharField(default=b'GR', max_length=2, null=True, blank=True, choices=[(b'NE', b'Nenhuma'), (b'LE', b'Leve'), (b'MO', b'Moderada'), (b'GR', b'Grave')]),
        ),
    ]
