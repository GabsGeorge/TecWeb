from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin

from core.models import Usuario
from core.models import Fornecedor
from core.models import Contratos
from core.models import Colaboradores
from core.models import Produto
from core.models import Categoria
# Usuario begin
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ["codigo_u","nome_u","usuario","senha","email_u","cpf","telefone_u","endereco_u","news"]
    search_fields = ["nome_u","usuario","cpf","email_u"]
    filter_horizontal = []
    ordering = ["codigo_u"]
    list_filter = []

class UsuarioForm(forms.ModelForm):
    def save(self, commit=True):
        Usuario = super(UsuarioForm,self).save(commit=False)
        Usuario.setpassword('123@mudar')
        if commit:
            Usuario.save()
        return Usuario
    
    class Meta:
        model = Usuario
        fields = ["codigo_u","nome_u","usuario","senha","email_u","cpf","telefone_u","endereco_u","news"]
      
class UsuarioAlteraForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["codigo_u","nome_u","usuario","senha","email_u","cpf","telefone_u","endereco_u","news"]
#Usuario end
#
#Produto begin
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["codigo_p","nome_f","nome_p","quantidade","categoria_p"]
    search_fields = ["nome_f","nome_p","categoria_p"]
    filter_horizontal = []
    ordering = ["categoria_p"]
    list_filter = []
#Produto end
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
    list_display = ["codigo_p","nome","sluga","criado","modificado",]
    search_fields = ["nome"]
    filter_horizontal = []
    ordering = ["nome"]
    list_filter = []
#Colaboradores end

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Fornecedor)
admin.site.register(Contratos)
admin.site.register(Produto)
admin.site.register(Colaboradores)
admin.site.register(Categoria)