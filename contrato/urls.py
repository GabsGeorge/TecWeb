# coding=utf-8

from django.conf.urls import url

from contrato import views

urlpatterns = [
    url(r'^contrato/adicionar/(?P<slug>[\w_-]+)', views.create_contratoitem, name='create_contratoitem'),
    url(r'^$', views.contrato_item, name='contrato_item'),
        url(r'^meus-contratos/$', views.lista_contrato, name='lista_contrato'),
    url(r'^detalhe-contratos/(?P<pk>\d+)/$', views.detalhe_contrato, name='detalhe_contrato'),

    url(r'^finalizando/$', views.checkout_contrato, name='checkout_contrato'),
    url(r'^finalizando1/$', views.registrodata, name='registrodata'),    
    #PagSeguro
    url(
        r'^finalizando/(?P<pk>\d+)/pagseguro/$', views.pagseguro_view,
        name='pagseguro_view'
    ),
    url(
        r'^notificacoes/pagseguro/$', views.pagseguro_notification,
        name='pagseguro_notification'
    ),
    #Paypal
    url(
        r'^finalizando/(?P<pk>\d+)/paypal/$', views.paypal_view,
        name='paypal_view'
    ),
]