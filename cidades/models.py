from django.db import models
from django.urls import reverse
from django.views import generic

class Cidade(models.Model):
    nome = models.CharField(max_length=150)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150)
    textinho = models.CharField(max_length=15000)
    foto_cidade = models.ImageField(upload_to= 'images')
    puzzle1 = models.ImageField(upload_to= 'images')
    puzzle2 = models.ImageField(upload_to= 'images')
    puzzle3 = models.ImageField(upload_to= 'images')
    puzzle4 = models.ImageField(upload_to= 'images')
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('euamovida-cidades', kwargs={'cidade_id': self.id})

class CategoryListView(generic.ListView):

    template_name = 'cidades/cidades.html'
    context_object_name = 'cidades'
    paginate_by = 3