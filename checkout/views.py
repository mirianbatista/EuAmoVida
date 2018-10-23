from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from django.contrib import messages

from lojinha.models import Produto

from .models import CartItem

class CreateCartItemView(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		produto = get_object_or_404(Produto, pk=self.kwargs['produto_id'])
		if self.request.session.session_key is None:
			self.request.session.save()
		cart_item, created = CartItem.objects.add_item(
			self.request.session.session_key, produto
		)
		if created:
			messages.success(self.request, 'Produto add com sucesso!')
		else:
			messages.success(self.request, 'Produto att com sucesso!')
		return produto.get_absolute_url()

create_cartitem = CreateCartItemView.as_view()