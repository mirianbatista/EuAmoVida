from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView, TemplateView 
from django.forms import modelformset_factory
from django.contrib import messages
from django.urls import reverse

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
		return reverse('cart_item')

class CartItemView(TemplateView):

	template_name = 'checkout/carrinho.html'

	def get_formset(self, clear=False):
		CartItemFormSet = modelformset_factory(
			CartItem, fields=('quantidade',), can_delete=True, extra=0
		)
		session_key = self.request.session.session_key
		if session_key:
			if clear:
				formset = CartItemFormSet(
					queryset = CartItem.objects.filter(cart_key=session_key),
				)
			else:
				formset = CartItemFormSet(
					queryset = CartItem.objects.filter(cart_key=session_key),
					data=self.request.POST or None
				)
		else:
			formset = CartItemFormSet(queryset=CartItem.objects.none())
		return formset


	def get_context_data(self, **kwargs):
		context = super(CartItemView, self).get_context_data(**kwargs)
		context['formset'] = self.get_formset()
		return context

	def post(self, request, *args, **kwargs):
		formset = self.get_formset()
		context = self.get_context_data(**kwargs)
		if formset.is_valid():
			formset.save()
			messages.success(request, 'Carrinho att aaa')
			context['formset'] = self.get_formset(clear=True)
		return self.render_to_response(context)

def index(request):
	return render(request, 'checkout/carrinho.html')

create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()