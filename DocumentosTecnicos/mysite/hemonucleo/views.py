from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from hemonucleo.forms import PostForm
from .models import *
# from django
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
# from .forms import NameForm

def index(request):
    latest_question_list = Doador.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def doacao(request):
    latest_question_list = Doacao.objects.order_by('-pub_date')[:5]
    template = loader.get_template('services.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.http import HttpResponseRedirect

# from .forms import NameForm

def name(request):
    latest_question_list = Doacao.objects.order_by('-pub_date')[:5]
    template = loader.get_template('name.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def post_new(request):
    form = PostForm()
    return render(request, 'name.html', {'form': form})


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
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