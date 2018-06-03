from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_admin, name="login_admin"),
    url(r'^cadastre-se/', views.registrar_admin, name="registrar_admin"),
]