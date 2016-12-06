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
    url(r'^doacao$', views.doacao, name='doacao'),
    url(r'^historico/$', views.historico, name='historico'),
    url(r'^doador/$', views.doador, name='doador'),
    url(r'^$', views.home, name='home'),
    url(r'^doador/(?P<nome>.+)/$', views.cadastroComSucesso, name="cadastroComSucesso"),
    url(r'^doador/cadastroComSucesso$', views.cadastroComSucesso, name="cadastroComSucesso"),
    url(r'^doacao/(?P<nome>.+)/$', views.cadastroComSucesso, name="cadastroComSucesso")
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)