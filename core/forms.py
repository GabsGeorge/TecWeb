from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from localflavor.br.forms import BRZipCodeField

from .models import Usuario, Cliente

class UserAdminCreationForm(UserCreationForm):
    zip_code = BRZipCodeField(label='CEP', max_length=9)
    street = forms.CharField(label='Rua', max_length=100)
    district = forms.CharField(label='Bairro', max_length=100)
    city = forms.CharField(label='Cidade', max_length=100)
    state = forms.CharField(label='Estado', max_length=100)
    
    class Meta:
        model = Cliente
        fields = ['username', 'name', 'second_name', 'email', 'cpf']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["name","username","email","cpf","telefone_u","endereco_u","news"]



class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome")
    email = forms.EmailField(label="E-mail") 
    telefone = forms.CharField(label="telefone")
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())

