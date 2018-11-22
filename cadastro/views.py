from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AdminPasswordChangeForm 
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView
from django.views import generic
from django.conf import settings 
from django.contrib import messages
from django.forms import modelformset_factory
from django.db import models


from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy, resolve
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import login as auth_login
from cadastro.forms import CriarCadastroUsuario, AlterarCadastroUsuario
from catalogo.models import Produto, Categoria
from cadastro.models import Cliente
from checkout.models import Pedido

from checkout.views import CartItemView

from django.shortcuts import render, redirect

from checkout.models import CartItem

from django.contrib.messages.views import SuccessMessageMixin

class MinhaContaView(LoginRequiredMixin, TemplateView):
    template_name = 'cadastro/minhaconta.html'
minhaconta = MinhaContaView.as_view()  



# -----------------------------------------------//---------------------------------#
# pagina de cadastro Usuário

class RegistroView(SuccessMessageMixin, CreateView):
    template_name = 'cadastro/registrar.html'
    model = Cliente
    form_class = CriarCadastroUsuario
    success_url = reverse_lazy('cadastro:login')
    success_message = "Seja bem vindo(a) %(nome)s, seu cadastro foi realizado com sucesso! "
registro = RegistroView.as_view()



# -----------------------------------------------//---------------------------------#
#funcao para alterar dados Usuário

class UpdateUserView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'cadastro/alterar-dados.html'
    model = Cliente
    form_class = AlterarCadastroUsuario
    success_url = reverse_lazy('cadastro:minhaconta')
    success_message = "Seus dados foram alterados com sucesso!"

    def get_object(self):
        return self.request.user
alterarusuario = UpdateUserView.as_view() 

# -----------------------------------------------//---------------------------------#
#funcao para alterar senha Usuário
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('cadastro:minhaconta')
        else:
            messages.error(request, 'Atenção! Verifique os erros abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'cadastro/alterar-senha.html', {
        'form': form
    })
# -----------------------------------------------//---------------------------------#

#funcao para alterar conigurações

#def config(request):
#    user = request.user
#
#    try:
#        github_login = user.social_auth.get(provider='github')
#    except UserSocialAuth.DoesNotExist:
#        github_login = None
#
#    try:
#        twitter_login = user.social_auth.get(provider='twitter')
#    except UserSocialAuth.DoesNotExist:
#        twitter_login = None
#
#    try:
#        facebook_login = user.social_auth.get(provider='facebook')
#    except UserSocialAuth.DoesNotExist:
#        facebook_login = None
#
#    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
#
#    return render(request, 'alterar-config.html', {
#        'github_login': github_login,
#        'twitter_login': twitter_login,
#        'facebook_login': facebook_login,
#        'can_disconnect': can_disconnect
#        })

# -----------------------------------------------//---------------------------------#