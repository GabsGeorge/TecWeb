from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import ContatoForm
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
from social_django.models import UserSocialAuth


from catalogo.models import Produto, Categoria
from checkout.models import Pedido

from checkout.views import CartItemView

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.messages.views import SuccessMessageMixin
from checkout.models import CartItem

Usuario = get_user_model()


class IndexView(ListView):
    model = Produto
    template_name = 'index.html'
    context_object_name = 'produtos'
    paginate_by = 9

index = IndexView.as_view()


def contato(request):
    success = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success

    }
    messages.success(request, 'Email enviado com successo')
    return render(request, 'contato.html', context)



class FestaView(TemplateView):
    template_name = 'festa.html'
festa = FestaView.as_view()    


class QuemsomosView(TemplateView):
    template_name = 'quemsomos.html'
quemsomos =  QuemsomosView.as_view()   


class ServicosView(TemplateView):
    template_name = 'servicos.html'
servicos = ServicosView.as_view()  


class CalculadoraView(TemplateView):
    template_name = 'calculadora.html'
calculadora =  CalculadoraView.as_view()


class NossasDicasView(TemplateView):
    template_name = 'nossasdicas.html'
nossasdicas =  NossasDicasView.as_view()  

