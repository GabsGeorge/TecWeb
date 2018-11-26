from django.contrib import admin

from catalogo.models import Produto
from catalogo.models import Categoria
from catalogo.models import Fornecedor
# Register your models here.

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


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Fornecedor)