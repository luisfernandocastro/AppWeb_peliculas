from django.db import models
from django.utils import timezone

# Create your models here.


class Pelicula(models.Model):
    name = models.CharField(db_column='Nombre',max_length=50,null=True)
    dateupload = models.DateTimeField(db_column='Fecha de subida',default=timezone.now)
    portada = models.ImageField(db_column='Portada',upload_to='portadaspelis')
    director = models.CharField(db_column='Director',max_length=100,null=True)
    descipcion = models.TextField(db_column='Descripcion',max_length=1000,null=True)
    


