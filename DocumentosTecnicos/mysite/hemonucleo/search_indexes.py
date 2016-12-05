import datetime
import django
import hemonucleo
from haystack import indexes
from hemonucleo.models import *


class DoadorSearch(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    nome = indexes.CharField(model_attr='nome')
    professor = indexes.CharField()

    def prepare_tag_name(self, object):
        return object.professor.nome

    def get_model(self):
        return Doador

    def index_queryset(self,using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter().all()
#
# class ArtigoSearch(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     nome = indexes.CharField(model_attr='titulo')
#
#     def get_model(self):
#         return Doacao
#
#     def index_queryset(self,using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter().all()
# #
# # class ProfessorSearch(indexes.SearchIndex, indexes.Indexable):
# #     text = indexes.CharField(document=True, use_template=True)
# #     nome = indexes.CharField(model_attr='nome')
# #
# #
# #     def get_model(self):
# #         return Professor
# #
# #     def index_queryset(self, using=None):
# #         return self.get_model().objects.filter().all()
