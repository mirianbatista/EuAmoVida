from django.db import models
from django.urls import reverse
from django.views import generic

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to= 'images')
    textinho = models.CharField(max_length=150, default="")
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['descricao']

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('euamovida-produto', kwargs={'produto_id': self.id})

class CategoryListView(generic.ListView):

    template_name = 'lojinha/loja.html'
    context_object_name = 'loja'
    paginate_by = 3