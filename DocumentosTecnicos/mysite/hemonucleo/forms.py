from django import forms

from hemonucleo.models import Doacao


class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ('doador', 'codigoDaAmostra','idade','outros','endereco','tipoDeDoacao','hospitalDeInternacao','procedimento', 'funcionario','data')
