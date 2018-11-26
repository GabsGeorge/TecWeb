from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
import re


class Cliente(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Username', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma'
    )

    SEXO_CHOICES = (
        ('M', u'Masculino'),
        ('F', u'Feminino'),
    )

    nome = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True, max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100, blank=True)
    rg = models.CharField("RG", max_length=13, null=True, blank=True) 
    cpf = models.CharField("CPF", unique=True, max_length=14)
    telefone_u = models.CharField("Nº telefone", max_length=14, blank=True, null=True)
    celular = models.CharField("Nº celular",max_length=16, blank=True, null=True)  # Field name made lowercase.
    news = models.NullBooleanField("Deseja receber novidades ?", db_column='News', default=True)  # Field name made lowercase. 
    nascimento = models.DateField(" Nascimento", blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    #Endereço
    cep = models.CharField('CEP', max_length=9)
    rua = models.CharField('Rua', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    numero = models.CharField('Número', blank=True, max_length=15)
    complemento = models.CharField('Complemento', max_length=100, blank=True)
    
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'cpf']

    objects = UserManager()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


