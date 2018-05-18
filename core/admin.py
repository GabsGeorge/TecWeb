from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from core.models import Cliente
from core.models import Fornecedor
from core.models import Contratos
from core.models import Colaboradores
from core.models import Produto
from core.models import Categoria
from core.models import Usuario


class ClienteForm(forms.ModelForm):
    def save(self, commit=True):
        cliente = super(UsuarioForm,self).save(commit=False)
        cliente.setpassword('123@mudar')
        cliente.perfil = "cliente"
        if commit:
            cliente.save()
        return cliente
    
    class Meta:
        model = Cliente
        fields = ["nome_u","user_name","email_u","cpf","telefone_u","endereco_u","news"]
      
class ClienteAlteraForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome_u","user_name","email_u","cpf","telefone_u","endereco_u","news"]


# Cliente begin
class ClienteAdmin(UserAdmin):
    add_form = ClienteForm
    form = ClienteAlteraForm
    add_fieldsets = ((None, { "fields": ("user_name", "nome_u", "email_u","cpf", "telefone_u", "endereco_u")}),)
    fieldsets = ((None, { "fields": ("nome_u", "email_u", "cpf")}),)
    list_display =["codigo_u","user_name","nome_u","email_u"]
    filter_horizontal = []
    ordering = ["codigo_u"]
    list_filter = ["nome_u"]

#Usuario end
#
#Produto begin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["codigo_p","nome_p","quantidade","categoria_p", "nome_f"]
    search_fields = ["nome_f","nome_p","categoria_p","codigo_p"]
    filter_horizontal = []
    ordering = ["codigo_p"]
    list_filter = []
    prepopulated_fields = {'slug': ('nome_p',)} # Cria url amigavel para navegador
#Produto end
#
#Categoria begin
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["codigo_p","nome","slug","criado","modificado",]
    search_fields = ["nome"]
    filter_horizontal = []
    ordering = ["nome"]
    list_filter = []
#Colaboradores end
#
#Fornecedor begin
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ["nome_f","email_f","endereco_f","telefoneprincipal","telefonesecundario","categoria_f"]
    search_fields = ["nome_f","categoria_f"]
    filter_horizontal = []
    ordering = ["categoria_f"]
    list_filter = []
#Fornecedor end
#
#Contratos begin
class ContratoAdmin(admin.ModelAdmin):
    list_display = ["codigo_u","descricao","dia","hora","endereco_ct"]
    search_fields = ["codigo_u","dia","endereco_ct"]
    filter_horizontal = []
    ordering = ["dia","hora"]
    list_filter = []
#Contratos end
#
#Colaboradores begin
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ["nome_c","codigo_c","telefone_c",]
    search_fields = ["nome_c"]
    filter_horizontal = []
    ordering = ["codigo_c"]
    list_filter = []
#Colaboradores end

#Categoria begin
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["codigo_cat","nome","slug","criado","modificado",]
    search_fields = ["nome"]
    filter_horizontal = []
    ordering = ["nome"]
    list_filter = []
    prepopulated_fields = {'slug': ('nome',)} # Cria url amigavel para navegador
#Colaboradores end

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Fornecedor)
admin.site.register(Contratos)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Colaboradores)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Usuario)