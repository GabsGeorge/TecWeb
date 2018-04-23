from django.conf.urls import url
from django.contrib import admin
from core.views import index 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name="index"),
    url(r'^$', index)
]

# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório 
#root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)