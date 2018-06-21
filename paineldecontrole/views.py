from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render # funcoes de renderizacao dos templates
from django.shortcuts import redirect # Funcao para executar um http-redirect

from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from django.contrib.auth.forms import AuthenticationForm # Formulario de autenticacao de usuarios
from django.contrib.auth import login # funcao que salva o usuario na sessao

# Create your views here.

def login_admin(request):
	return render(request, "paineldecontrole/login.html")

def index(request):
	return render(request, "paineldecontrole/index.html")	   

def registrar_admin(request):
    return render(request, "paineldecontrole/registrar_admin.html")  

#Auntenticação Usuario
@login_required(login_url="entrar")
def page_user(request):
    return render(request,"paineldecontrole/index.html")

