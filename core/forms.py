from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

class ContatoForm(forms.Form):
    nome = forms.CharField(label="nome")
    email = forms.EmailField(label="E-mail") 
    telefone = forms.CharField(label="telefone")
    message = forms.CharField(label="message", widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        message = self.cleaned_data['message']
        message = 'Nome: {0}\nE-mail:{1}\n{2}'.format(nome, email, telefone, message)
        send_mail(
            'Contato do Django E-Commerce', message, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
        )

