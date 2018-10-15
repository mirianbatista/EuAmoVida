from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=9,decimal_places=2)
    quantidade = models.IntegerField()
    

def __init__(self):
    return self.descricao