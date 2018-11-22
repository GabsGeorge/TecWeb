   # coding: utf-8
from django.db import models
from django.conf import settings
from catalogo.models import Produto
from pagseguro import PagSeguro
from django.db.models import Avg

#Carrinho de compras----
class ContratoItemManager(models.Manager):

    def add_item_item(self, contrato_key, produto):
        if self.filter(contrato_key=contrato_key, produto=produto).exists():
            created = False
            contrato_item = self.get(contrato_key=contrato_key, produto=produto)
            contrato_item.quantidade = contrato_item.quantidade + 1
            
            contrato_item.save()
        else:
            created = True
            contrato_item = ContratoItem.objects.create(contrato_key=contrato_key, produto=produto, preco_p=produto.preco_p)
            
        return contrato_item, created

#Item do Carrinho de compras --
class ContratoItem(models.Model):

    contrato_key = models.CharField('Chave do Contrato', max_length=40, db_index=True)
    produto = models.ForeignKey('catalogo.Produto', verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco_p = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    

    objects = ContratoItemManager()

    class Meta:
        verbose_name = 'Item do contrato'
        verbose_name_plural = 'Itens dos contratos'
        unique_together = (('contrato_key', 'produto'),)

    def __str__(self):
        return '{} [{}]'.format(self.produto, self.quantidade)

def post_save_contrato_item(instance, **kwargs):
    if instance.quantidade < 1:
        instance.delete()


models.signals.post_save.connect(
    post_save_contrato_item, sender=ContratoItem, dispatch_uid='post_save_contrato_item'
)


class PedidoContratoManager(models.Manager):
    def criacao_pedido(self, user, contrato_items):
        pedido = self.create(user=user)
        for contrato_item in contrato_items:
            item_do_contrato = ItemDoContrato.objects.create(
                pedido=pedido, quantidade=contrato_item.quantidade, produto=contrato_item.produto,
                preco_p=contrato_item.preco_p
            )
        return pedido

class Contrato(models.Model):

    STATUS_CHOICES=(
        (0, 'Aguardando pagamento'),
        (1, 'Concluída'),
        (2, 'Cancelada'),
    )

    OPCOES_DE_PAGAMENTO=(
        ('deposito', 'Depósito'),
        ('pagseguro', 'PagSeguro'),
        ('paypal', 'PayPal'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário')
    status = models.IntegerField('Situacao', choices=STATUS_CHOICES, default=0, blank=True)  
    opcoes_de_pagamento = models.CharField('Opcao de pagamento', choices=OPCOES_DE_PAGAMENTO, max_length=20, default= 'deposito') 


    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    objects = PedidoContratoManager()

    class Meta:
        verbose_name='Contrato'
        verbose_name_plural='Contratos'

    def __str__(self):
        return 'PedidoContrato#{}'.format(self.pk)

    def produtos(self):
        produtos_ids = self.items.values_list('produto')
        return Produto.objects.filter(pk__in=produtos_ids)

    def total(self):
        aggregate_queryset = self.items.aggregate(
            total=models.Sum(
                models.F('preco_p') * models.F('quantidade'),
                output_field=models.DecimalField()
            )
        )
        return aggregate_queryset['total']

    #forma de pagamento PagSeguro --
    def pagseguro_update_status(self, status):
        if status == '3':
            self.status = 1
        elif status == '7':
            self.status = 2
        self.save()

    def complete(self):
        self.status = 1
        self.save()

    def pagseguro(self):
        self.opcoes_de_pagamento = 'pagseguro'
        self.save()
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )

        pg.sender = {
            'email': self.user.email
        }
        pg.reference_prefix = ''    
        pg.shipping = None  
        pg.reference = self.pk
        for item in self.items.all():
            pg.items.append(
                {
                    'id': item.produto.pk,
                    'description': item.produto.nome_p,
                    'quantity': item.quantidade,
                    'amount': '%.2f' % item.preco_p
                }
            )
        return pg


    def paypal(self):
        self.opcoes_de_pagamento = 'paypal'
        self.save()
        paypal_dict = {
            'upload': '1',
            'business': settings.PAYPAL_EMAIL,
            'invoice': self.pk,
            'cmd': '_cart',
            'currency_code': 'BRL',
            'charset': 'utf-8',
        }
        index = 1
        for item in self.items.all():
            paypal_dict['amount_{}'.format(index)] = '%.2f' % item.preco_p
            paypal_dict['item_name_{}'.format(index)] = item.produto.nome_p
            paypal_dict['quantity_{}'.format(index)] = item.quantidade
            index = index + 1
        return paypal_dict
    
    

#items do pedido --
class ItemDoContrato(models.Model):
    pedido = models.ForeignKey(Contrato, verbose_name='Contrato', related_name='items')
    produto = models.ForeignKey('catalogo.Produto', verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco_p = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.pedido, self.produto)


class DataContrato(models.Model):
    Contrato = models.ForeignKey(Contrato, verbose_name='Contrato')
    data = models.DateField('Dados do contrato')

