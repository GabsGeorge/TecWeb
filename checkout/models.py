from django.db import models
from django.conf import settings


#Carrinho----
class CartItemManager(models.Manager):

    def add_item(self, cart_key, produto):
        if self.filter(cart_key=cart_key, produto=produto).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, produto=produto)
            cart_item.quantidade = cart_item.quantidade + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(
                cart_key=cart_key, produto=produto, preco_p=produto.preco_p
            )
        return cart_item, created


class CartItem(models.Model):

    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
    )
    produto = models.ForeignKey('catalogo.Produto', verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco_p = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('cart_key', 'produto'),)

    def __str__(self):
        return '{} [{}]'.format(self.produto, self.quantidade)


def post_save_cart_item(instance, **kwargs):
    if instance.quantidade < 1:
        instance.delete()


models.signals.post_save.connect(
    post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)




class PedidoManager(models.Manager):
    def criacao_pedido(self, user, cart_items):
        pedido = self.create(user=user)
        for cart_item in cart_items:
            item_do_pedido = ItemDoPedido.objects.create(
                pedido=pedido, quantidade=cart_item.quantidade, produto=cart_item.produto,
                preco_p=cart_item.preco_p
            )
        return pedido
        



#Pedido ------
class Pedido(models.Model):

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
    opcoes_de_pagamento = models.CharField('Opcao de pagamento', choices=OPCOES_DE_PAGAMENTO, max_length=20, 
        default= 'deposito') 

    criado = models.DateTimeField('Criado em', auto_now_add=True)
    modificado = models.DateTimeField('Modificado em', auto_now=True)

    objects = PedidoManager()

    class Meta:
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'

    def __str__(self):
        return 'Pedido #{}'.format(self.pk)
    


class ItemDoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', related_name='items')
    produto = models.ForeignKey('catalogo.Produto', verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco_p = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens dos pedidos'

    def __str__(self):
        return '[{}] {}'.format(self.pedido, self.produto)   
        


        

