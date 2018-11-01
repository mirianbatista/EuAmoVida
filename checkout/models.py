from django.db import models

class CartItemManager(models.Manager):
	def add_item(self, cart_key,produto):
		if self.filter(cart_key=cart_key, produto=produto).exists():
			created = False
			cart_item = self.get(cart_key=cart_key, produto=produto)
			cart_item.quantidade = cart_item.quantidade + 1
			cart_item.save()
		else:
			created = True
			cart_item = CartItem.objects.create(
				cart_key=cart_key, produto=produto, preco=produto.preco
			)			
		return cart_item, created

class CartItem(models.Model):
	cart_key = models.CharField('Chave do carrinho', max_length=40, db_index=True)
	produto = models.ForeignKey('lojinha.Produto', verbose_name='Produto', on_delete=models.CASCADE)
	quantidade = models.PositiveIntegerField('Quantidade', default=1)
	preco = models.DecimalField('Preço', max_digits=9,decimal_places=2)

	objects = CartItemManager()
	

	class Meta:
		verbose_name = 'Item do carrinho'
		verbose_name_plural = 'Itens do carrinho'
		unique_together = (('cart_key', 'produto'),)

	def __str__(self):
		return '{} [{}]'.format(self.produto, self.quantidade)


def post_save_cart_item(instance, **kwargs):
	if instance.quantidade < 1:
		instance.delete()

models.signals.post_save.connect(
	post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item'
)