from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50,)
    short_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    annulate = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return self.name + '-' + self.short_name