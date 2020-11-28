from django.urls import path
from .views import VistaHome, BlogDetalle, CrearBlog, EditarBlog, BorrarBlog, CrearCarrera, CarreraView, Comentar
from django.urls import include

urlpatterns = [
    #path('', views.home, name="home"),
    path('', VistaHome.as_view(), name = 'home'),
    path('noticia/<int:pk>', BlogDetalle.as_view(), name = 'blog_detalle'),
    path('crear_noticia/', CrearBlog.as_view(), name = 'crear_blog'),
    path('crear_carrera/', CrearCarrera.as_view(), name='crear_carrera'),
    path('noticia/editar/<int:pk>', EditarBlog.as_view(), name='editar_blog'),
    path('noticia/<int:pk>/eliminar', BorrarBlog.as_view(), name='borrar_blog'),
    path('carreras/<str:carreras>/', CarreraView, name='carreras'),
    path('noticia/<int:pk>/comentar', Comentar.as_view(),name='comentar'),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft'))

]
