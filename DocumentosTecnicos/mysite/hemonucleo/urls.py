from django.conf.urls import url

from django.contrib import admin
from django.views.generic import TemplateView

from mysite import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from hemonucleo import views
from django.conf.urls import handler400, handler403, handler404, handler500

admin.autodiscover()

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^doacao$', views.doacao, name='doacao'),
    url(r'^historico/$', views.historico, name='historico'),
    url(r'^doador/$', views.doador, name='doador'),
    url(r'^$', views.home, name='home'),
    url(r'^doador/(?P<nome>.+)/$', views.cadastroComSucesso, name="doador"),

#     urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^/curso$', views.curso, name='curso'),
#     url(r'^/professor$', views.professor, name='professor'),
#     url(r'^/projeto$', views.projetos, name='projetos'),
#     url(r'^/evento$', views.eventos, name='eventos'),
#     url(r'^/publicacao$', views.publicacao, name='publicacao'),
#     url(r'^/curso/(?P<sigla_curso>.+)/$', views.detailCurso, name='detailCurso'),
#     url(r'^/curso/(?P<sigla_curso>.+)/(?P<ementa>.+)$', views.detailCursoEmenta, name='detailCursoEmenta'),
#     url(r'^/professor/(?P<professor_nome>.+)$', views.detailsProfessor, name='details'),
#     url(r'^/projeto/(?P<projeto_nome>.+)$', views.detailsProjeto, name='detailsProjeto'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)