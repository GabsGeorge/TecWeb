from django import forms
from django.contrib.auth.forms import UserCreationForm
from cadastro.models import Cliente


class CriarCadastroUsuario(UserCreationForm):
 
    class Meta:
        model = Cliente
        fields = ['username', 'nome', 'sobrenome', 'email', 'cpf' ,'nascimento', 'telefone_u', 'celular','cep','rua', 'bairro', 'cidade', 'estado', 'numero', 'password1', 'password2']


class AlterarCadastroUsuario(forms.ModelForm):
 
    class Meta:
        model = Cliente
        fields = ['username', 'nome', 'sobrenome', 'email', 'cpf', 'rg' ,'nascimento', 'telefone_u', 'celular','cep','rua', 'bairro', 'cidade', 'estado', 'numero', 'complemento']



#-------Ajuste Admin Django----------

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = Cliente
        fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['username', 'email', 'nome', 'is_active', 'is_staff']

#-------------------


