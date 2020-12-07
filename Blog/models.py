from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse_lazy
from datetime import datetime, date

#CARRERAS DISPONIBLES
class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse_lazy('blog_detalle', args=str(self.id))

#MODELO DE NOTICIA
class Blog(models.Model):
    autor_id = models.ForeignKey(User, on_delete = models.CASCADE)
    titulo = models.CharField(max_length=50, blank = False, null = False)
    cuerpo = RichTextField()
    fecha = models.DateField(auto_now_add=True)
    carrera = models.CharField(max_length=50, default='General')

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor_id)

    def get_absolute_url(self):
        return reverse_lazy('blog_detalle', args=str(self.id))

#MODELO DE COMENTARIO
class Comentario(models.Model):
    blog = models.ForeignKey(Blog, related_name="comentario", on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    cuerpo = RichTextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.blog.titulo, self.nombre)


