from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.views import generic
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

from core.forms import ClienteForm, EditaContaClienteForm, ContatoForm
from catalogo.models import Produto, Categoria



class IndexView(generic.ListView):
    model = Produto
    template_name = 'index.html'
    context_object_name = 'produtos'
    paginate_by = 8
index = IndexView.as_view()


def contato(request):
    form = contatoForm
    contexto = {
        "categorias":Categoria.objects.all(),
        'form':form
    }
    return render(request, "contato.html", contexto)

def festa(request):
    contexto = {
        "categorias":Categoria.objects.all()

    }
    return render(request,"festa.html", contexto)

def quemsomos(request):
    contexto = {
        "categorias":Categoria.objects.all()
    }
    return render(request,"quemsomos.html", contexto)


#Autenticação login
def login_cliente(request):
    return render(request,"login.html")

def contato(request):
    return render(request,"contato.html")

#Auntenticação Usuario
@login_required(login_url="entrar")
def page_user(request):
    return render(request,'index.html')



# -----------------------------------------------//---------------------------------#

# pagina de cadastro
def registrar(request):    
     # Se dados forem passados via POST
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid(): # se o formulario for valido
            form.save() # cria um novo usuario a partir dos dados enviados
            form.cleaner
    else:
        form = ClienteForm()
    contexto = {
        "form":form
    }
    return render(request, "registrar.html", contexto)


# -----------------------------------------------//---------------------------------#

#funcao para alterar conta
@login_required
def editarConta(request):
    template_name = 'editarConta.html'
    contexto = {}
    if request.method == 'POST':
        form = EditaContaClienteForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditaContaClienteForm(instance=request.user)
            contexto['success'] = True
    else:
        form = EditaContaClienteForm(instance=request.user)
    contexto['form'] = form
    return render(request, template_name, contexto)

# -----------------------------------------------//---------------------------------#

#funcao para alterar senha
@login_required
def editarSenha(request):
    template_name = 'editarSenha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)   

    # -----------------------------------------------//---------------------------------#