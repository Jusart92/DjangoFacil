from django.db import models

# Create your models here.

class Mascota(models.Model):
    # Django genera pk default si no tenemos una
    folio = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
