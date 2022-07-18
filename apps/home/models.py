from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.
class Lembrete(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    status = models.BooleanField()
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
