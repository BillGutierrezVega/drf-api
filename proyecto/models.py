from django.db import models

# Create your models here.
class Proyectos(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=150)
    creado = models.DateTimeField(auto_now_add=True)