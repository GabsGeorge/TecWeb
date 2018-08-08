from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings

from core import views
from catalogo import views as catalogo_views
from paineldecontrole import views as paineldecontrole_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/', views.index, name="index"),
    
    # begin url app Catalogo,
    url(r'^catalogo/', include('catalogo.urls')),
    # end url app Catalogo

    # begin url app Painel de Controle,
    url(r'^easyparty/', include('paineldecontrole.urls')),
    # end url app Painel de Controle

    url(r'^contato/', views.contato, name="contato"),
    url(r'^festas/', views.festa, name="festas"),
    url(r'^registrar/',views.registrar, name='registrar'),
    url(r'^quemsomos/',views.quemsomos, name='quemsomos'),
    

    url(r'^login', login, { "template_name":"login.html" }, name='entrar'),
    url(r'^logout',logout, { "next_page":"index.html" }, name="sair"),
    
    

]

# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório 
#root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)