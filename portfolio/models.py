from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")  # Campo de caracteres
    decription = models.TextField(verbose_name="Descripción")  # Campo de texto
    image = models.ImageField(verbose_name="Imagen", upload_to='projects')  # Campo de imagenes
    link = models.URLField(null=False,blank=True, verbose_name="Dirección Web")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")  # Se ejecuna la primera vez que se crea
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualización")  # Se ejecuata cada que se actualiza una instancia

    class Meta:
        verbose_name = "proyecto"  # Nombre de la tabla
        verbose_name_plural = "proyectos"  # Nombre de la tabla en plural
        ordering = ["-created"]  # Columna por la cual se ordenara la información, el - indica que es al reves

    def __str__(self):
        return self.title
