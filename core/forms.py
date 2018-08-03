from django import forms
from core.models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ["nome_u","user_name","email_u","cpf","telefone_u","endereco_u","news"]



class ContatoForm(forms.ModelForm):
    nome = forms.CharField(label="nome")
    email = forms.EmailField(label="E-mail") 
    telefone = forms.CharField(label="telefone")
    mensagem = forms.CharField(label="mensagem", widget=forms.Textarea())

        

class EditaContaClienteForm(forms.ModelForm):

    def clean_email(self):
    #Verifica se Email ja está cadastrado para poder editar    
        email = self.cleaned_data['email_u']
        queryset = Cliente.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email

    class Meta:
        model = Cliente
        fields = ('nome_u','email_u','telefone_u', 'endereco_u')