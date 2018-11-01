from django.db import models
from django.urls import reverse
from django.views import generic

class Colabore(models.Model):
    doacao = models.CharField(max_length=150, default="")
    imagem = models.ImageField(upload_to= 'images')
    textinho = models.CharField(max_length=1500, default="")
    def __str__(self):
        return self.doacao

    class Meta:
        verbose_name = 'Colabore'
        verbose_name_plural = 'Doações'
        ordering = ['doacao']

    def __str__(self):
        return self.doacao

    def get_absolute_url(self):
        return reverse('euamovida-colabore', kwargs={'doacao_id': self.id})

class CategoryListView(generic.ListView):

    template_name = 'colabore/colabore.html'
    context_object_name = 'colabore'
    paginate_by = 3