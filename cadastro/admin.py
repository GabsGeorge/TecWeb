# coding=utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Cliente
from .forms import UserAdminCreationForm, UserAdminForm


class UsuarioAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('username', 'nome', 'sobrenome', 'email', 'cpf', 'rg' ,'nascimento', 'telefone_u', 'celular','cep','rua', 'bairro', 'cidade', 'estado', 'numero', 'complemento')
        }),
        ('Informações Básicas', {
            'fields': ('nome', 'last_login')
        }),
        (
            'Permissões', {
                'fields': (
                    'is_active', 'is_staff', 'is_superuser', 'groups',
                    'user_permissions'
                )
            }
        ),
    )
    list_display = ['username', 'nome', 'email', 'is_active', 'is_staff', 'date_joined']

admin.site.register(Cliente, UsuarioAdmin)