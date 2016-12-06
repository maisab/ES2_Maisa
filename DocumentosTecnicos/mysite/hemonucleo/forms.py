from django import forms
from hemonucleo.models import Doacao, Doador

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ('doador', 'codigoDaAmostra','idade','outros','endereco','tipoDeDoacao','hospitalDeInternacao','procedimento', 'funcionario','data')

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ('nome', 'endereco','idade','outrosDados','nomeDoPai','nomeDoMae','sexo','estadoCivil', 'nacionalidade','RG', 'orgaoExpedidor', 'CPF', 'profissao','trabalhoAtual', 'municipio', 'estado', 'telefone', 'celular', 'email')

from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'usuario'}))
    password = forms.CharField(label="Senha", max_length=15,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'senha'}))