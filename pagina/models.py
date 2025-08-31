from django.db import models

class  Cigarro(models.Model):
    marca=models.CharField(max_length=20)
    cantidad=models.CharField(max_length=20)
   
    def __str__(self):
     return f'{self.marca} {self.cantidad}'