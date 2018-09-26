from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from core.models import Cliente
from core.models import Contrato
from core.models import Colaborador
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
        fields = ["name","username","email","cpf","telefone_u","endereco_u","news"]
      
class ClienteAlteraForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["name","username","email","cpf","telefone_u","endereco_u","news"]


# Cliente begin
class ClienteAdmin(UserAdmin):
    add_form = ClienteForm
    form = ClienteAlteraForm
    add_fieldsets = ((None, { "fields": ("username", "name", "email","cpf", "telefone_u", "endereco_u")}),)
    fieldsets = ((None, { "fields": ("name", "email", "cpf")}),)
    list_display =["codigo_u","username","name","email", 'is_staff', 'is_active', 'date_joined']
    filter_horizontal = []
    ordering = ["codigo_u"]
    list_filter = ["name"]

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
admin.site.register(Contrato)
admin.site.register(Colaborador, ColaboradoresAdmin)
admin.site.register(Usuario)