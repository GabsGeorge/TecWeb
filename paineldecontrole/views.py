from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login # funcao que salva o usuario na sessao
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class LoginView(generic.ListView):
	template_name = 'paineldecontrole/login.html'
	success_url = reverse_lazy('index')
login = LoginView.as_view()


class IndexContaView(LoginRequiredMixin, TemplateView):
    template_name = 'paineldecontrole/index.html'
index = IndexContaView.as_view()  
	   

class RegistrarView(TemplateView):  
    template_name = 'paineldecontrole/registrar_admin.html'
registrar = RegistrarView.as_view()  

