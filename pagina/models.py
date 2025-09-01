from django.db import models


class Products(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='products/')

class Contacts(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()


class Testimonials(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()
    imagem = models.ImageField(upload_to='testimonials/')


class Gallery(models.Model):
    imagem = models.ImageField(upload_to='gallery/')