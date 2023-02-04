from django.db import models

# Create your models here.
class Pessoa (models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True);
    idade = models.IntegerField(max_length=3, null=True, blank=True);
    id_dep = models.IntegerField(max_length=3, null=True, blank=True);
    