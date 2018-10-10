# coding=utf-8

from django.conf.urls import url

from location import views

urlpatterns = [
    url(r'^contrato/adicionar/(?P<slug>[\w_-]+)', views.create_contratoitem, name='create_contratoitem'),
    url(r'^contrato/', views.contrato_item, name='contrato_item'),

]