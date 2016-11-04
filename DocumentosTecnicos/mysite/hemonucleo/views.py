from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

from .models import *
# from django
from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Context, loader


def index(request):
    latest_question_list = Doador.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

