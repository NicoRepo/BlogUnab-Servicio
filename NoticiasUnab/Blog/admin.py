from django.contrib import admin
from .models import Blog, Carrera, Comentario
# Register your models here.

# admin.site.register(Autor)
admin.site.register(Blog)
admin.site.register(Carrera)
admin.site.register(Comentario)

