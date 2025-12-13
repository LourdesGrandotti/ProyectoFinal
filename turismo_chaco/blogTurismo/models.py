from django.db import models

# Create your models here.
class Destino(models.Model):
    id_destino=models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_Length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    categoria = models.CharField(
        max_length=50,
        choices=[
            ("Naturaleza", "Naturaleza"),
            ("Cultura", "Cultura"),
            ("Gastronomia", "Gastronomia"),
        ]
    )

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    id_evento=models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_Length=200)
    fecha = models.DateField()
    lugar = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="eventos/", blank=True, null=True)

def __str_(self):
    return F"{self.titulo} - {self.fecha}"
