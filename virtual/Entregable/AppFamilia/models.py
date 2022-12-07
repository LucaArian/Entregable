from django.db import models
class familiar(models.Model):
    nombre=models.CharField(max_length=40)
    edad= models.IntegerField()
    fecha= models.DateField()

# Create your models here.
