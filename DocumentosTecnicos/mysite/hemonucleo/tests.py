# -*- coding: UTF-8 -*-
# -*- encoding: UTF-8 -*-
# Create your tests here.
from hemonucleo.models import *
from django.test import TestCase


class ProfessorTestCase(TestCase):
    def setUp(self):

        doador = Doador(nome="Humberto")
        doador.save()


    def testDoadorHumberto(self):
        d = Doador.objects.get(nome="Humberto")
        self.assertEquals(d.nome, "Humberto")

