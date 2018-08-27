from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Usuario, Cliente

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'cpf']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["name","username","email","cpf","telefone_u","endereco_u","news"]



class ContatoForm(forms.ModelForm):
    nome = forms.CharField(label="nome")
    email = forms.EmailField(label="E-mail") 
    telefone = forms.CharField(label="telefone")
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())

        