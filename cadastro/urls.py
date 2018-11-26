# coding=utf-8

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from django.contrib.auth.views import login, logout, password_reset

from cadastro import views

urlpatterns = [
    # begin url app Conta
    url(r'^usuario/minhaconta/',views.minhaconta, name='minhaconta'),
    url(r'^usuario/alterar-usuario/',views.alterarusuario, name='alterarusuario'),
    url(r'^usuario/alterar-senha/',views.change_password, name='alterarsenha'),
    #url(r'^usuario/configuracoes/',views.config, name='config'),
    url(r'^registrar/',views.registro, name='registrar'),
    url(r'^login/', login,{"template_name":"cadastro/login.html" }, name='login'),
    url(r'^logout/$', logout, {'next_page': 'index'}, name='logout'),

 
]