from django.contrib import admin

# Register your models here.
from hemonucleo.models import Doador, Doacao

admin.site.register(Doador)
admin.site.register(Doacao)
