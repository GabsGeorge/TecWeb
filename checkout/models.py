from django.db import models

# Create your models here.

class ItemCarrinhoManager(models.Manager):
	def add_item(self, carrinho_key, produto):
		carrinho_item, created = self.get_or_create(carrinho_key=carrinho_key, produto=produto)
		if not created:
			carrinho_item.quantidade = carrinho_item.quantidade + 1
			carrinho_item.save()
			return carrinho_item

class ItemCarrinho(models.Model):
    carrinho_key = models.CharField('Chave do Carrinho', max_length=40, db_index=True)
    produto = models.ForeignKey('catalogo.Produto', verbose_name='Produto')
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco_p = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens dos Carrinhos'
        unique_together = (('carrinho_key', 'produto'),)

    def __str__(self):
        return '{} [{}]'.format(self.produto, self.quantidade)
			    	
