from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    quantidade = models.IntegerField()
   # imagem = models.FileField(upload_to= 'post_image', blank=True)
    def __str__(self):
        return self.descricao