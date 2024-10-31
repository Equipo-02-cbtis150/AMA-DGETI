from django.db import models

# Create your models here.

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(default='default@example.com')
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} - {self.comentario} - {self.email}"
    