from jet.dashboard.dashboard_modules import google_analytics_views

from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
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


    url(r'^, include', include('django.contrib.auth.urls')),
    
    # begin url app Catalogo,
    url(r'^catalogo/', include('catalogo.urls')),
    # end url app Catalogo

    # begin url app Checkout
    url(r'^compras/', include('checkout.urls', namespace='checkout')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    # end url app Checkout

    # begin url app location
    url(r'^contrato/', include('contrato.urls', namespace='contrato')),
    # end url app location

    # begin url app cadastro
    url(r'^cadastro/', include('cadastro.urls', namespace='cadastro')),
    # end url app cadatro


    url(r'^contato/', views.contato, name="contato"),
    url(r'^festas/', views.festa, name="festas"),
    url(r'^quemsomos/',views.quemsomos, name='quemsomos'),
    url(r'^servicos/',views.servicos, name='servicos'),
    url(r'^calculadora/',views.calculadora, name='calculadora'),
    url(r'^nossasdicas/',views.nossasdicas, name='nossasdicas'),


 



    #Social Login
    url(r'^auth/', include('social_django.urls', namespace='social')),
    # end url app Conta 

    #begin newsletter
    url(r'^newsletter/', include('newsletter.urls')),
    #end newsletter 
]   

# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório 
#root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)