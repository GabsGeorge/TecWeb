# coding=utf-8
import json

from django.db import models


from pagseguro import PagSeguro

from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    RedirectView, TemplateView, ListView, DetailView, View, CreateView
)
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse


from catalogo.models import Produto
from contrato.models import PedidoContrato

from .models import CartItemContrato, ItemDoPedidoContrato


class CreateCartItemView(View):

    def get(self, request, *args, **kwargs):
        produto = get_object_or_404(Produto, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()

        cart_item, created = CartItemContrato.objects.add_item(
            self.request.session.session_key, produto
        )
        if created:
            message = 'Produto adicionado no contrato com sucesso'
        else:
            message = 'Produto atualizado com sucesso'
        if request.is_ajax():
            return HttpResponse(
                json.dumps({'message': message}), content_type='application/javascript'
            )
        messages.success(request, message)
        return redirect('contrato:cart_item')
       
create_cartitem = CreateCartItemView.as_view()


class CartItemView(TemplateView):

    template_name = 'contrato/cart.html'

    def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItemContrato, fields=('quantidade',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset=CartItemContrato.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset=CartItemContrato.objects.filter(cart_key=session_key),
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItemContrato.objects.none())
        return formset

    def get_context_data(self, **kwargs):
       context = super(CartItemView, self).get_context_data(**kwargs)
       context['formset'] = self.get_formset()
       session_key = self.request.session.session_key
       if session_key:
           cart_items = CartItemContrato.objects.filter(cart_key=session_key)
           aggregate_queryset = cart_items.aggregate(
                total=models.Sum(
                    models.F('preco_p') * models.F('quantidade'),
                    output_field=models.DecimalField()
                )
            )
           context["total"] = aggregate_queryset['total'] or 0
       else:
           context["total"] = 0
       return context


    def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)
  
cart_item = CartItemView.as_view()



class CheckoutView(LoginRequiredMixin, TemplateView):

    template_name = 'contrato/checkout_contrato.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CartItemContrato.objects.filter(cart_key=session_key).exists():
            cart_items = CartItemContrato.objects.filter(cart_key=session_key)
            pedido = PedidoContrato.objects.criacao_pedido(
                user=request.user, cart_items=cart_items
            )
            cart_items.delete()
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('contrato:cart_item')
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        response.context_data['pedido'] = pedido
        return response

checkout = CheckoutView.as_view()


class ListaDePedidoView(LoginRequiredMixin, ListView):
    template_name = "contrato/lista_contrato.html"
    paginate_by = 10
    def get_queryset(self):
        return PedidoContrato.objects.filter(user=self.request.user)
lista_contrato = ListaDePedidoView.as_view()


class DetalhePedidoView(LoginRequiredMixin, DetailView):
    template_name = 'contrato/detalhe_contrato.html'
    def get_queryset(self):
        return PedidoContrato.objects.filter(user=self.request.user)
detalhe_contrato = DetalhePedidoView.as_view()



class PagSeguroView(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        pedido_pk = self.kwargs.get('pk')
        pedido = get_object_or_404(
            PedidoContrato.objects.filter(user=self.request.user), pk=pedido_pk
        )
        pg = pedido.pagseguro()
        pg.redirect_url = self.request.build_absolute_uri(
            reverse('contrato:detalhe_contrato', args=[pedido.pk])
        )
        pg.notification_url = self.request.build_absolute_uri(
            reverse('contrato:pagseguro_notification')
        )

        response = pg.checkout()
        return response.payment_url
pagseguro_view = PagSeguroView.as_view()


@csrf_exempt
def pagseguro_notification(request):
    notification_code = request.POST.get('notificationCode', None)
    if notification_code:
        pg = PagSeguro(

            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        notification_data = pg.check_notification(notification_code)
        status = notification_data.status
        reference = notification_data.reference
        try:
            pedido = PedidoContrato.objects.get(pk=reference)
        except PedidoContrato.DoesNotExist:
            pass
        else:
            pedido.pagseguro_update_status(status)
    return HttpResponse('OK')



class PaypalView(LoginRequiredMixin, TemplateView):

    template_name = 'checkout/paypal.html'

    def get_context_data(self, **kwargs):
        context = super(PaypalView, self).get_context_data(**kwargs)
        pedido_pk = self.kwargs.get('pk')
        pedido = get_object_or_404(
            PedidoContrato.objects.filter(user=self.request.user), pk=pedido_pk
        )
        paypal_dict = pedido.paypal()
        paypal_dict['return_url'] = self.request.build_absolute_uri(
            reverse('contrato:lista_contrato')
        )
        paypal_dict['cancel_return'] = self.request.build_absolute_uri(
            reverse('contrato:lista_contrato')
        )
        paypal_dict['notify_url'] = self.request.build_absolute_uri(
            reverse('paypal-ipn')
        )
        context['form'] = PayPalPaymentsForm(initial=paypal_dict)
        return context

paypal_view = PaypalView.as_view()


def paypal_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED and \
        ipn_obj.receiver_email == settings.PAYPAL_EMAIL:
        try:
            pedido = PedidoContrato.objects.get(pk=ipn_obj.invoice)
            pedido.complete()
        except PedidoContrato.DoesNotExist:
            pass
valid_ipn_received.connect(paypal_notification)

