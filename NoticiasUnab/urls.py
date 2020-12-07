from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('', include('tutorial.urls')),
    path('usuarios/', include('django.contrib.auth.urls')), #Defecto
    path('usuarios/', include('usuarios.urls')), #Personalizadas
]
