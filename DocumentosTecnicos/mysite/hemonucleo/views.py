from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from hemonucleo.forms import DoacaoForm, DoadorForm
from .models import *
# from django
from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
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

def doacao(request):
    latest_question_list = Doacao.objects.order_by('-pub_date')[:5]
    template = loader.get_template('doacao.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def doacao(request):

    form = DoacaoForm()
    return render(request, 'doacao.html', {'form': form})

def historico(request):
    form = DoacaoForm()
    return render(request, 'historico.html', {'form': form})

def cadastroComSucesso(request,nome):
    post =  Doador.objects.get(nome=nome)
    return render(request, 'cadastroComSucesso.html', {'post': post})

def doador(request):
    if request.method == "POST":
        form = DoadorForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('cadastroComSucesso', nome=post.nome)
    else:
        form = DoadorForm()

    return render(request,  'doador.html', {'form': form})

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