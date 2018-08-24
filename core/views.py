from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView
from django.views import generic
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy

from core.forms import ClienteForm, EditaContaClienteForm, ContatoForm, UserAdminCreationForm
from catalogo.models import Produto, Categoria
from core.models import Cliente


Usuario = get_user_model()


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


class FestaView(CreateView):
    template_name = 'festa.html'
festa = FestaView.as_view()    


class QuemsomosView(CreateView):
    template_name = 'quemsomos.html'
quemsomos =  QuemsomosView.as_view()   


class ServicosView(TemplateView):
    template_name = 'servicos.html'
servicos = ServicosView.as_view()  


class MinhaContaView(LoginRequiredMixin, TemplateView):
    template_name = 'minhaconta.html'
minhaconta = MinhaContaView.as_view()  


# -----------------------------------------------//---------------------------------#
# pagina de cadastro

class RegistroView(CreateView):
    template_name = 'registrar.html'
    model = Usuario
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('minhaconta')
registro = RegistroView.as_view()


# -----------------------------------------------//---------------------------------#
#funcao para alterar dados

class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'alterar-dados.html'
    model = Cliente
    fields = ['name', 'email', 'cpf']
    success_url = reverse_lazy('minhaconta')

    def get_object(self):
        return self.request.user
alterarusuario = UpdateUserView.as_view() 

# -----------------------------------------------//---------------------------------#
#funcao para alterar senha

class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'alterar-senha.html'
    success_url = reverse_lazy('minhaconta')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
alterarsenha = UpdatePasswordView.as_view() 

# -----------------------------------------------//---------------------------------#