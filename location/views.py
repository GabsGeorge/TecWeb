import json

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    RedirectView, TemplateView, ListView, DetailView, View
)
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse


from catalogo.models import Produto
from checkout.models import Pedido

from location.models import ContratoItem


class CreateContratoItemView(View):

    def get(self, request, *args, **kwargs):
        produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()

        contrato_item, created = ContratoItem.objects.add_item_item(
            self.request.session.session_key, produto
        )
        if created:
            message = 'Produto adicionado no contrato com sucesso'
        else:
            message = 'Produto atualizado no contrato com sucesso'
        if request.is_ajax():
            return HttpResponse(
                json.dumps({'message': message}), content_type='application/javascript'
            )
        messages.success(request, message)
        return redirect('location:contrato_item')
       
create_contratoitem = CreateContratoItemView.as_view()


class ContratoItemView(TemplateView):

    template_name = 'location/contrato_aluguel.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            ContratoItem, fields=('quantidade',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=ContratoItem.objects.filter(contrato_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=ContratoItem.objects.filter(contrato_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=ContratoItem.objects.none())
        return formset

    def get_context_data(self, **kwargs):
        context = super(ContratoItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context


    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)

contrato_item = ContratoItemView.as_view()
