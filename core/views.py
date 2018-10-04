from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AdminPasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView
from django.views import generic
from django.conf import settings 
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy, resolve
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from social_django.models import UserSocialAuth

from core.forms import ContatoForm, UserAdminCreationForm
from catalogo.models import Produto, Categoria
from core.models import Cliente
from checkout.models import Pedido

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect



Usuario = get_user_model()


from django.utils.translation import ugettext_lazy as _
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
from jet.dashboard.dashboard_modules import google_analytics


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
       self.available_children.append(google_analytics.GoogleAnalyticsVisitorsTotals)
       self.available_children.append(google_analytics.GoogleAnalyticsVisitorsChart)
       self.available_children.append(google_analytics.GoogleAnalyticsPeriodVisitors)


class IndexView(ListView):
    model = Produto
    template_name = 'index.html'
    context_object_name = 'produtos'
    paginate_by = 8

index = IndexView.as_view()


def contato(request):
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            email = form.cleaned_data["email"]
            telefone = form.cleaned_data["telefone"]
            mensagem = form.cleaned_data["mensagem"]
            try:
               send_mail(nome,email,telefone,mensagem['lcs.amorim.lima@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect("troxa")    
    return render(request, "contato.html", {"formula":form})


class FestaView(TemplateView):
    template_name = 'festa.html'
festa = FestaView.as_view()    


class QuemsomosView(TemplateView):
    template_name = 'quemsomos.html'
quemsomos =  QuemsomosView.as_view()   


class ServicosView(TemplateView):
    template_name = 'servicos.html'
servicos = ServicosView.as_view()  


class MinhaContaView(LoginRequiredMixin, TemplateView):
    template_name = 'minhaconta.html'
minhaconta = MinhaContaView.as_view()  


class CalculadoraView(TemplateView):
    template_name = 'calculadora.html'
calculadora =  CalculadoraView.as_view() 



# -----------------------------------------------//---------------------------------#
# pagina de cadastro Usuário

class RegistroView(CreateView, FormView):
    template_name = 'registrar.html'
    model = Usuario
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('minhaconta')
    #messages.success('Cadastro realizado com sucesso')
registro = RegistroView.as_view()


# -----------------------------------------------//---------------------------------#
#funcao para alterar dados Usuário

class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = 'alterar-dados.html'
    model = Cliente
    fields = ['username', 'name', 'second_name', 'email', 'cpf', 'telefone_u','endereco_u','news']
    success_url = reverse_lazy('minhaconta')

    def get_object(self):
        return self.request.user
alterarusuario = UpdateUserView.as_view() 

# -----------------------------------------------//---------------------------------#
#funcao para alterar senha Usuário

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

#funcao para alterar conigurações

def config(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'alterar-config.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
        })

# -----------------------------------------------//---------------------------------#