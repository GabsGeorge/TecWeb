import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class Colaborador(models.Model):
    nome_c = models.CharField(db_column='Nome_C', max_length=100)  # Field name made lowercase.
    codigo_c = models.AutoField(db_column='Codigo_C', primary_key=True)  # Field name made lowercase.
    telefone_c = models.IntegerField(db_column='Telefone_C')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Colaboradores'


class Contrato(models.Model):
    codigo_u = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Codigo_U')  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase.
    dia = models.DateField(db_column='Dia')  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
    endereco_ct = models.CharField(db_column='Endereco_CT', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Contratos'

class Usuario(AbstractBaseUser, PermissionsMixin):

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
    codigo_u = models.AutoField(db_column='Codigo_U', primary_key=True)  # Field name made lowercase.
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]



class Cliente(Usuario):
    cpf = models.IntegerField("CPF", db_column='CPF', unique=True)  # Field name made lowercase.
    telefone_u = models.IntegerField("Telefone", db_column='Telefone_U')  # Field name made lowercase.
    endereco_u = models.CharField("Endereço", db_column='Endereco_U', max_length=255)  # Field name made lowercase.
    news = models.NullBooleanField("Deseja receber novidades ?", db_column='News', blank=True)  # Field name made lowercase.
        




