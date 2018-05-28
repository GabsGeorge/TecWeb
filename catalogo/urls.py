from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.lista_produto, name="lista_produto"),

]