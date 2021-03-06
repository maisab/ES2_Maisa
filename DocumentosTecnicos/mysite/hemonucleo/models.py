from datetime import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Funcionario(models.Model):
    nome = models.CharField('Nome do Funcionario',max_length=200)
    permissao = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome


class Gerente(models.Model):
    nome = models.CharField('Nome do Gerente',max_length=200)

class Doador(models.Model):
    nome = models.CharField('Nome do Doador',max_length=200)
    endereco = models.CharField('Endereco',max_length=200)
    idade = models.IntegerField(default=0)
    outrosDados = models.CharField('Outros', max_length=200, blank=True, null=True)
    nomeDoPai = models.CharField('Nome do Pai', max_length=200, blank=True, null=True )
    nomeDoMae = models.CharField('Nome do Mae', max_length=200, blank=True, null=True)

    masculino = 'M'
    feminino = 'F'

    genero = (
        (masculino, 'Masculino'),
        (feminino, 'Feminino'),
    )
    sexo = models.CharField(max_length=1, choices=genero,default=masculino)

    solteiro = 'S'
    casado = 'C'
    outros = 'O'
    tipo = (
        (solteiro, 'Solteiro'),
        (casado, 'Casado'),
        (outros, 'Outros'),
    )
    estadoCivil = models.CharField(max_length=1, choices=tipo, default=solteiro, blank=True, null=True)

    nacionalidade = models.CharField('Nacionalidade', max_length=200, blank=True, null=True)
    RG = models.CharField('RG', max_length=15, blank=True, null=True)
    orgaoExpedidor =models.CharField('Orgao Expedidor', max_length=10, blank=True, null=True)
    CPF =models.CharField('CPF', max_length=20, blank=True, null=True)
    profissao = models.CharField('Profissao', max_length=100, blank=True, null=True)
    trabalhoAtual = models.CharField('Trabalho Atual', max_length=200, blank=True, null=True)
    municipio= models.CharField('Municipio', max_length=200, blank=True, null=True)
    estado = models.CharField('Estado', max_length=200, blank=True, null=True)
    telefone = models.CharField('Telefone', max_length=200, blank=True, null=True)
    celular = models.CharField('celular', max_length=200, blank=True, null=True)
    email =models.EmailField()

    def __unicode__(self):
        return  "{0}, {1}, {2},{3}".format(self.nome, self.email, self.telefone, self.celular)




class Doacao(models.Model):
    doador = models.ForeignKey(Doador,on_delete=models.CASCADE)
    codigoDaAmostra = models.IntegerField('Codigo da Amostra', default=000000)
    endereco = models.CharField('Endereco',max_length=200, blank=True, null=True)
    idade = models.IntegerField(default=0, blank=True, null=True)
    outros = models.CharField('Outros', max_length=200, blank=True, null=True)


    espontanea = 'ES'
    convocada= 'CO'
    reposicao = 'RE'
    autologa ='AU'
    tipo = (
        (espontanea, 'Espontanea'),
        (convocada, 'Convocada'),
        (reposicao, 'Reposicao'),
        (autologa, 'Autologa'),
    )
    tipoDeDoacao = models.CharField(max_length=2, choices=tipo, default=espontanea)
    hospitalDeInternacao =  models.CharField('Hospital de Internacao', max_length=200, blank=True, null=True)
    coletaConvencional = 'CC'
    aferese= 'AF'

    tipo = (
        (coletaConvencional, 'Coleta Convencional'),
        (aferese, 'Aferese'),
    )
    procedimento = models.CharField(max_length=2, choices=tipo, default=coletaConvencional)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    data = models.DateTimeField(default=datetime.now, blank=True)


class UltimaDoacao(models.Model):
    peso =models.CharField('Peso da amostra',max_length=10, blank=True, null=True)
    hematocrito =models.CharField("Hematocrito", max_length=10, blank=True, null=True)
    hemoglobina = models.CharField('Hemoglobina', max_length=10, blank=True, null=True)
    pulso = models.CharField('Pulso', max_length=10, blank=True, null=True)
    pressaoArterial = models.CharField('Pressao Arterial', max_length=10, blank=True, null=True)
    apto = 'AP'
    inapto = 'IN'
    inaptoTemporariamente ='IT'

    tipo = (
        (apto, 'Apto'),
        (inapto, 'Inapto'),
        (inaptoTemporariamente, 'Inapto Temporariamente')
    )
    data = models.DateTimeField(default=datetime.now, blank=True, null=True)
    apto = models.CharField(max_length=2, choices=tipo, default=inapto, blank=True, null=True)
    nenhuma = 'NE'
    leve = 'LE'
    moderada ='MO'
    grave ='GR'
    tipo = (
        (nenhuma, 'Nenhuma'),
        (leve, 'Leve'),
        (moderada, 'Moderada'),
        (grave, 'Grave')
    )
    # data = models.DateTimeField(default=datetime.now, blank=True)
    reacoes = models.CharField(max_length=2, choices=tipo, default=grave, blank=True, null=True)
    descricaoDaReacao = models.CharField('Pulso', max_length=200)


class Historico(models.Model):
    descricao = models.IntegerField(default=0, blank=True, null=True)
    historico = models.CharField(max_length=1000, blank=True, null=True)
    votes = models.IntegerField(default=0, blank=True, null=True)
    doador = models.ForeignKey(Doador, on_delete=models.CASCADE)