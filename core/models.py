from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    
    def _criar_usuario(self, user_name, password, **campos):
        if not user_name:
            raise ValueError('username deve ser declarado!')
        user = self.model(user_name=user_name, **campos)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, user_name, password=None, **campos):
        return self._criar_usuario(user_name, password,**campos)

    def create_superuser(self, user_name, password=None, **campos):
        campos.setdefault('perfil','adm')
        return self._criar_usuario(user_name, password,**campos)


class Colaboradores(models.Model):
    nome_c = models.CharField(db_column='Nome_C', max_length=100)  # Field name made lowercase.
    codigo_c = models.AutoField(db_column='Codigo_C', primary_key=True)  # Field name made lowercase.
    telefone_c = models.IntegerField(db_column='Telefone_C')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Colaboradores'


class Contratos(models.Model):
    codigo_u = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Codigo_U')  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase.
    dia = models.DateField(db_column='Dia')  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora')  # Field name made lowercase.
    endereco_ct = models.CharField(db_column='Endereco_CT', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Contratos'


class Fornecedor(models.Model):
    nome_f = models.CharField(db_column='Nome_F', primary_key=True, max_length=100)  # Field name made lowercase.
    email_f = models.CharField(db_column='Email_F', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endereco_f = models.CharField(db_column='Endereco_F', max_length=255)  # Field name made lowercase.
    telefoneprincipal = models.IntegerField(db_column='TelefonePrincipal')  # Field name made lowercase.
    telefonesecundario = models.IntegerField(db_column='TelefoneSecundario', blank=True, null=True)  # Field name made lowercase.
    categoria_f = models.CharField(db_column='Categoria_F', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.nome_f

    class Meta:
        managed = True
        db_table = 'Fornecedor'


class Categoria(models.Model):
    codigo_cat = models.AutoField(db_column='Codigo_cat', primary_key=True)  
    nome = models.CharField("Nome" ,max_length=100)
    slug = models.SlugField("Identificador", max_length=100)
    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("modificado em", auto_now_add=True)
    imagem = models.ImageField(db_column='Imagem',upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


class Produto(models.Model):
    codigo_p = models.AutoField(db_column='Codigo_P', primary_key=True)  # Field name made lowercase.
    nome_f = models.ForeignKey(Fornecedor, models.DO_NOTHING, db_column='Nome Fornecedor')  # Field name made lowercase.
    nome_p = models.CharField("Nome do produto", db_column='Nome_P', max_length=100)  # Field name made lowercase.
    quantidade = models.SmallIntegerField("Quantidade", db_column='Quantidade')  # Field name made lowercase.
    categoria_p = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_p')  # Field name made lowercase.
    imagem = models.ImageField("Imagem", db_column='Imagem',upload_to='media')
    descricao = models.TextField("Descrição",db_column='Descricao_P')
    custo_p = models.DecimalField("Custo", decimal_places=2, max_digits=10, db_column='Custo_P')
    preco_p = models.DecimalField("Preço", decimal_places=2, max_digits=10, db_column='Preço_P')
    
    slug = models.SlugField("Identificador", max_length=100)
    vender = models.BooleanField(db_column='Vender', default=True)
    ativo = models.BooleanField(db_column='Ativo',default=True)
    criado = models.DateTimeField("Criado em", auto_now_add=True)
    modificado = models.DateTimeField("modificado em", auto_now_add=True)

    def __str__(self):
        return self.nome_p

    class Meta:
        managed = True
        db_table = 'Produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['codigo_p']  


class Usuario(AbstractBaseUser):
    codigo_u = models.AutoField(db_column='Codigo_U', primary_key=True)  # Field name made lowercase.
    nome_u = models.CharField("Nome",db_column='Nome_U', max_length=255)  # Field name made lowercase.
    user_name = models.CharField("username",db_column='user_name', unique=True, max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='password', max_length=200)  # Field name made lowercase.
    email_u = models.EmailField("E-mail",db_column='Email_U', max_length=100, blank=True, null=True)  # Field name made lowercase.
    perfil = models.CharField("Perfil", max_length=1)
    Ativo = models.BooleanField("Ativo", default=True)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ["nome_u","email_u"]
    objects = UsuarioManager()

    class Meta:
        managed = True
        db_table = 'Usuario'


    def get_full_name(self):
        return self.nome_u

    def get_short_name(self):
        return self.nome_u

    def __str__(self):
        return self.nome_u

    @property
    def is_staff(self):
        return self.perfil == "adm"

    def has_module_perms(self, package_name):
        return True

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True


class Cliente(Usuario):
    cpf = models.IntegerField("CPF", db_column='CPF', unique=True)  # Field name made lowercase.
    telefone_u = models.IntegerField("Telefone", db_column='Telefone_U')  # Field name made lowercase.
    endereco_u = models.CharField("Endereço", db_column='Endereco_U', max_length=255)  # Field name made lowercase.
    news = models.NullBooleanField("Deseja receber novidades ?", db_column='News', blank=True)  # Field name made lowercase.
        


    # --------------------------------------------------------------------- // ------------------------------------------------------------#

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
