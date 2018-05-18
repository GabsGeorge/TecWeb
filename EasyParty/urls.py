from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings

from core.views import categoria
from core.views import editarConta
from core.views import editarSenha

from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/', views.index, name="index"),
    url(r'^produto/', views.produto, name="produto"),
    url(r'^produtos/', views.lista_produto, name="lista_produto"),
    url(r'^contato/', views.contato, name="contato"),
    url(r'^festas/', views.festa, name="festa"),
    url(r'^registrar/',views.registrar, name='registrar'),

    url(r'^login', login, { "template_name":"login.html" }, name='entrar'),
    url(r'^logout',logout, { "next_page":"index.html" }, name="sair"),
    #url(r'^(?P<slug>[\w_-]+)/$', produto),
    

    url(r'^(?P<slug>[\w_-]+)/$', views.categoria),

    
     # pagina de cadastro
    url(r'^editar-conta', editarConta, name="editar-conta"),
    url(r'^editar-senha', editarSenha, name="editar-senha"),
]

# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório 
#root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)