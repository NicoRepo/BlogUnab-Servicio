from django.test import TestCase
from models import Blog, Comentario
from django.contrib.auth.models import User
from datetime import datetime, date

class BlogModelTest(TestCase):
    
    def setUp(self):
        self.autor_id = User.objects.create(username='testuser', password='2344153156')
        self.titulo ="Noticia"
        self.carrera = "Carrera"
        self.fecha = datetime.now()
        self.cuerpo = "asd"
        self.blog = Blog(autor_id=self.autor_id, titulo=self.titulo, fecha=self.fecha, carrera=self.carrera)

        self.post = Blog(autor_id=self.autor_id, titulo=self.titulo, fecha=self.fecha, carrera=self.carrera)
        self.nombre = "Juanito"
        self.fecha = datetime.now()
        self.comentario = Comentario(nombre=self.nombre, fecha=self.fecha, blog=self.post)

    def test_creacionBlog(self):
        old_count = Blog.objects.count()
        self.blog.save()
        new_count = Blog.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_creacionComentario(self):
        old_count = Comentario.objects.count()
        self.post.save()
        self.comentario.save()
        new_count = Comentario.objects.count()
        self.assertNotEqual(old_count, new_count)