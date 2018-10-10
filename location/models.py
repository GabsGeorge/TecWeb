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
