from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=24)
    email = models.EmailField(max_length=120)
    observacao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
