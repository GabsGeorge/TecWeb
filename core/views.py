from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


from core.forms import ClienteForm, EditaContaClienteForm
from core.models import Produto
from core.models import Categoria




def index(request):
    contexto = {
        "produtos":Produto.objects.all()
    }
    return render(request, "index.html", contexto)  

def produto(request): #, slug):
    #contexto = {
    #    'produto': get_object_or_404(Produto, slug=slug) #verifica se a url existe, caso nao exista ele retorna erro 404
    #}
    template_name = 'produto.html'
    return render(request, template_name)   

def lista_produto(request):
    pass


def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)  
    contexto = {
        'categoria': categoria, 
        'produtos': Produto.objects.filter(categoria=categoria),
       
    }
    return render(request,'categoria.html', contexto) 


def contato(request):
    pass


def login_cliente(request):
    return render(request,"login.html")

def contato(request):
    return render(request,"contato.html")

def festa(request):
    return render(request,"festa.html")

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