from jet.dashboard.dashboard_modules import google_analytics_views

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views

from core import views
from catalogo import views as catalogo_views

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index/', views.index, name="index"),
    
    # begin url app Catalogo,
    url(r'^catalogo/', include('catalogo.urls')),
    # end url app Catalogo

    # begin url app Checkout
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # end url app Checkout

    # begin url app location
    url(r'^locacao/', include('location.urls', namespace='location')),
    # end url app location

    url(r'^contato/', views.contato, name="contato"),
    url(r'^festas/', views.festa, name="festas"),
    url(r'^registrar/',views.registro, name='registrar'),
    url(r'^quemsomos/',views.quemsomos, name='quemsomos'),
    url(r'^servicos/',views.servicos, name='servicos'),
    url(r'^calculadora/',views.calculadora, name='calculadora'),
    url(r'^nossas-dicas/',views.NossasDicas, name='nossasDicas'),

    # begin url app Conta
    url(r'^usuario/minhaconta/',views.minhaconta, name='minhaconta'),
    url(r'^usuario/alterar-usuario/',views.alterarusuario, name='alterarusuario'),
    url(r'^usuario/alterar-senha/',views.alterarsenha, name='alterarsenha'),
    url(r'^usuario/configuracoes/',views.config, name='config'),
    url(r'^login/', login, { "template_name":"login.html" }, name='login'),
    url(r'^logout/$', logout, {'next_page': 'index'}, name='logout'),


    #Social Login
    url(r'^auth/', include('social_django.urls', namespace='social')),
    # end url app Conta    
    

]

# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório 
#root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)