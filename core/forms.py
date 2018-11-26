from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome")
    email = forms.EmailField(label="E-mail") 
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        mensagem = 'Nome: {0}\nE-mail:{1}\n{2}'.format(nome, email, mensagem)
        send_mail(
            'Contato de Cliente', mensagem, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )

