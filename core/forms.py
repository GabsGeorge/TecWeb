from django import forms
from django.contrib.auth.forms import UserCreationForm
from localflavor.br.forms import BRZipCodeField
from .models import Usuario

class UserAdminCreationForm(UserCreationForm):
 
    class Meta:
        model = Usuario
        fields = ['username', 'name', 'second_name', 'email', 'cpf' , 'telefone_u']

class UserAdminAlteraCadastro(UserCreationForm):
 
    class Meta:
        model = Usuario
        fields = ['username', 'name', 'second_name', 'email', 'cpf' ,'rg', 'telefone_u', 'zip_code', 'street', 'district', 'city', 'state', 'number', 'password1', 'password2']

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'name', 'is_active', 'is_staff']




class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome")
    email = forms.EmailField(label="E-mail") 
    telefone = forms.CharField(label="telefone")
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())

