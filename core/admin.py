from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from core.models import Cliente
from core.models import Contratos
from core.models import Colaboradores
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


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Contratos)
admin.site.register(Colaboradores)
admin.site.register(Usuario)