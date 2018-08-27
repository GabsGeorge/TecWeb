from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
    url(r'^$', login, { "template_name":"paineldecontrole/login.html" }, name='entrar'),
    url(r'^login/', login, { "template_name":"paineldecontrole/login.html" }, name='entrar'),
    url(r'^logout/',logout, { "next_page":"paineldecontrole/index.html" }, name="sair"),    
    url(r'^cadastre-se/', views.registrar_admin, name="registrar_admin"),
    url(r'^index/', views.index, name="registrar_admin"),


 ]