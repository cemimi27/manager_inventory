from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    senha = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)


class CategoriaProduto(models.Model):
    nome_categoria = models.CharField(max_length=50)


class Produto(models.Model):
    nome_produto = models.CharField(max_length=200)
    cod_produto = models.CharField(max_length=10)
    cod_barras = models.CharField(max_length=13)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, max_places=2)
    categoria = models.ForeignKey(
        CategoriaProduto, on_delete=models.SET_NULL, null=True
    )
