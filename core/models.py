from django.db import models

class Colaboradores(models.Model):
    nome_c = models.CharField(db_column='Nome_C', max_length=100)  # Field name made lowercase.
    codigo_c = models.AutoField(db_column='Codigo_C', primary_key=True)  # Field name made lowercase.
    telefone_c = models.IntegerField(db_column='Telefone_C')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Colaboradores'


class Contratos(models.Model):
    codigo_u = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Codigo_U')  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase.
    dia = models.DateField(db_column='Dia')  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
    endereco_ct = models.CharField(db_column='Endereco_CT', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contratos'


class Fornecedor(models.Model):
    nome_f = models.CharField("Nome do Fornecedor",db_column='Nome_F', primary_key=True, max_length=100)  # Field name made lowercase.
    email_f = models.CharField(db_column='Email_F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endereco_f = models.CharField(db_column='Endereco_F', max_length=255)  # Field name made lowercase.
    telefoneprincipal = models.IntegerField(db_column='TelefonePrincipal')  # Field name made lowercase.
    telefonesecundario = models.IntegerField(db_column='TelefoneSecundario', blank=True, null=True)  # Field name made lowercase.
    categoria_f = models.CharField(db_column='Categoria_F', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.nome_f

    class Meta:
        managed = False
        db_table = 'Fornecedor'


class Produto(models.Model):
    codigo_p = models.AutoField("Codigo do produto", db_column='Codigo_P', primary_key=True)  # Field name made lowercase.
    nome_f = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='Nome_F')  # Field name made lowercase.
    nome_p = models.CharField("Titulo do produto", db_column='Nome_P', max_length=100)  # Field name made lowercase.
    quantidade = models.SmallIntegerField("Quantidade", db_column='Quantidade')  # Field name made lowercase.
    categoria_p = models.CharField("Categoria", db_column='Categoria_P', max_length=100)  # Field name made lowercase.
    imagem = models.ImageField("Imagem do Produto",upload_to='banco_de_imagens', null=True, blank=True)
    descricao = models.TextField('Especificação do produto', blank=True)
    custo_p = models.IntegerField("Custo do produto",db_column='Custo_p')
    preco_p = models.IntegerField("Valor de venda", db_column='Preco_p')
    vender = models.BooleanField("Vender ?",default=True)
    ativo = models.BooleanField("Ativo ?",default=True)


    class Meta:
        managed = False
        db_table = 'Produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome_p']  

    def __str__(self):
        return self.nome_p
            
class Usuario(models.Model):
    codigo_u = models.AutoField(db_column='Codigo_U', primary_key=True)  # Field name made lowercase.
    nome_u = models.CharField(db_column='Nome_U', max_length=255)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=100)  # Field name made lowercase.
    senha = models.CharField(db_column='Senha', max_length=100)  # Field name made lowercase.
    email_u = models.CharField(db_column='Email_U', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cpf = models.IntegerField(db_column='CPF', unique=True)  # Field name made lowercase.
    telefone_u = models.IntegerField(db_column='Telefone_U')  # Field name made lowercase.
    endereco_u = models.CharField(db_column='Endereco_U', max_length=255)  # Field name made lowercase.
    news = models.NullBooleanField(db_column='News')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
