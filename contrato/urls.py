# coding=utf-8

from django.conf.urls import url

from contrato import views

urlpatterns = [
    url(r'^carrinho/adicionar/(?P<slug>[\w_-]+)', views.create_cartitem, name='create_cartitem'),
    url(r'^carrinho/', views.cart_item, name='cart_item'),
    url(r'^finalizando/$', views.checkout, name='checkout'),


    url(r'^meus-contratos/$', views.lista_contrato, name='lista_contrato'),
    url(r'^detalhe-contratos/(?P<pk>\d+)/$', views.detalhe_contrato, name='detalhe_contrato'),

    

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
    url(r'^finalizando/(?P<pk>\d+)/paypal/$', views.paypal_view,name='paypal_view'),
]