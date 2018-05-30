from django.conf.urls import url
from catalogo import views

urlpatterns = [
    url(r'^$', views.lista_produto, name="lista_produto"),
    url(r'^(?P<slug>[\w_-]+)/$', views.categoria, name="categoria"),
]