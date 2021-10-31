from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Card(models.Model):
    texto = models.CharField(max_length=400)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(null=True)
    tags = models.ForeignKey(Tag, verbose_name="tags", on_delete=models.CASCADE)

    def _str_(self):
        return self.texto

