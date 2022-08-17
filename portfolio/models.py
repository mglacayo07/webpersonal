from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)  # Campo de caracteres
    decription = models.TextField()  # Campo de texto
    image = models.ImageField()  # Campo de imagenes
    created = models.DateTimeField(auto_now_add=True)  # Se ejecuna la primera vez que se crea
    updated = models.DateTimeField(auto_now=True)  # Se ejecuata cada que se actualiza una instancia
