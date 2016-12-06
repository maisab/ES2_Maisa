from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.core.urlresolvers import reverse

from hemonucleo.forms import DoacaoForm, DoadorForm
from .models import *
# from django
from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .forms import NameForm

def index(request):
    latest_question_list = Doador.objects.order_by('nome')
    template = loader.get_template('home.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# def doacao(request):
#     latest_question_list = Doacao.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('doacao.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# def doador(request):
#     if request.method == "POST":
#         form = DoadorForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             # post.author = request.user
#             # post.published_date = timezone.now()
#             post.save()
#             return redirect('cadastroComSucesso', pk=post.pk)
#     else:
#         form = Doador()
#     return render(request, 'doador.html', {'form': form})

def historico(request):

    doacoes = Doacao.objects.all().order_by('data')
    paginator = Paginator(doacoes, 10)
    page = request.GET.get('page')
    try:
        historia = paginator.page(page)
    except PageNotAnInteger:
        historia = paginator.page(1)
    except EmptyPage:
        historia= paginator.page(paginator.num_pages)
    return render_to_response('historico.html', {"historico": historia})


def cadastroComSucesso(request):
    latest_question_list = Doador.objects.order_by('nome')
    template = loader.get_template('cadastroComSucesso.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# from django.contrib.auth.decorators import permission_required
# @permission_required('hemonucleo.pode_mudar_status')
def doador(request):
    if request.method == "POST":
        form = DoadorForm(request.POST)
        if form.is_valid():
            novo = form.cleaned_data['nome']
            endereco = form.cleaned_data[ 'endereco']
            idade = form.cleaned_data[ 'idade']
            outrosDados = form.cleaned_data['outrosDados']
            nomeDoPai = form.cleaned_data[ 'nomeDoPai']
            nomeDoMae = form.cleaned_data[ 'nomeDoMae']
            sexo = form.cleaned_data[ 'sexo']
            estadoCivil = form.cleaned_data[ 'estadoCivil']
            nacionalidade = form.cleaned_data[ 'nacionalidade']
            RG = form.cleaned_data[ 'RG']
            CPF = form.cleaned_data[ 'CPF']
            profissao = form.cleaned_data[ 'profissao']
            orgaoExpedidor = form.cleaned_data[ 'orgaoExpedidor']
            trabalhoAtual = form.cleaned_data[ 'trabalhoAtual']
            municipio = form.cleaned_data[ 'municipio']
            estado = form.cleaned_data[ 'estado']
            telefone = form.cleaned_data[ 'telefone']
            celular = form.cleaned_data[ 'celular']
            email = form.cleaned_data[ 'email']
            post = Doador.objects.create(nome=novo,endereco=endereco,idade=idade,outrosDados=outrosDados,
                                         nomeDoPai=nomeDoPai,nomeDoMae=nomeDoMae,sexo=sexo,estadoCivil=estadoCivil,
                                        nacionalidade=nacionalidade,RG=RG,CPF=CPF,profissao=profissao,orgaoExpedidor=orgaoExpedidor,
                                         trabalhoAtual =trabalhoAtual,municipio=municipio,estado=estado,telefone=telefone,
                                         celular=celular,email=email)

            return HttpResponseRedirect('cadastroComSucesso')

    else:
        form = DoadorForm()
    return render(request,  'doador.html', {'form': form})

def doacao(request):
    if request.method == "POST":
        form = DoacaoForm(request.POST)
        if form.is_valid():
            fields = (
            'doador', 'codigoDaAmostra', 'idade', 'outros', 'endereco', 'tipoDeDoacao', 'hospitalDeInternacao',
            'procedimento', 'funcionario', 'data')
            doador = form.cleaned_data['doador']
            codigoDaAmostra = form.cleaned_data[ 'codigoDaAmostra']
            idade = form.cleaned_data[ 'idade']
            outros = form.cleaned_data['outros']
            endereco = form.cleaned_data[ 'endereco']
            tipoDeDoacao = form.cleaned_data[ 'tipoDeDoacao']
            hospitalDeInternacao = form.cleaned_data[ 'hospitalDeInternacao']
            procedimento = form.cleaned_data[ 'procedimento']
            funcionario = form.cleaned_data[ 'funcionario']
            data = form.cleaned_data[ 'data']
            post = Doador.objects.create(doador=doador,codigoDaAmostra=codigoDaAmostra,idade=idade,outros=outros,
                                         endereco=endereco,tipoDeDoacao=tipoDeDoacao,hospitalDeInternacao=hospitalDeInternacao,
                                         procedimento=procedimento,funcionario=funcionario,RG=RG,data=data)

            return HttpResponseRedirect('cadastroComSucesso')

    else:
        form = DoacaoForm()
    return render(request,  'doacao.html', {'form': form})

# @permission_required('hemonucleo.pode_mudar_status')
def doacao(request):
    if request.method == "POST":
        form = DoacaoForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('cadastroComSucesso', nome=post.nome)
    else:
        form = DoacaoForm()

    return render(request,  'doacao.html', {'form': form})
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':r
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})

#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
    latest_question_list = Doacao.objects.order_by('-data')
    template = loader.get_template('home.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # return (request,"home.html")