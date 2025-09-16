from django.db import models

class  Cigarro(models.Model):
    marca=models.CharField(max_length=20)
    cantidad=models.CharField(max_length=20)
    imagen=models.ImageField(upload_to='cigarros', null=True, blank=True)
   
    def __str__(self):
     return f'{self.marca} {self.cantidad}'