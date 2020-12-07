from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Blog, Carrera, Comentario
from .forms import BlogForm, BlogEditForm, ComentarioForm
from django.urls import reverse_lazy


class VistaHome(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'home.html'
    login_url = '/usuarios/login/'
    #ordering = ['-id'] #Se mostrara primero la ultima ID
    ordering = ['-fecha']

    def get_context_data(self, *args, **kwargs):
        carr_menu = Carrera.objects.all()
        context = super(VistaHome, self).get_context_data(*args, **kwargs)
        context["carr_menu"] = carr_menu
        return context

@login_required(login_url='/usuarios/login/')
def CarreraView(request, carreras):
    #REPARAR NOMBRE DE URL*
    carr_menu = Carrera.objects.all()
    carrera_noticias = Blog.objects.filter(carrera=carreras.replace('-', ' '))
    return render(request, 'carreras.html', {'carreras': carreras.title().replace('-', ' '), 'carrera_noticias': carrera_noticias, 'carr_menu': carr_menu})

class BlogDetalle(LoginRequiredMixin , DetailView):
    model = Blog
    login_url = '/usuarios/login/'
    template_name = 'blog_detalle.html'

    def get_context_data(self, *args, **kwargs):
        carr_menu = Carrera.objects.all()
        context = super(BlogDetalle, self).get_context_data(*args, **kwargs)
        context["carr_menu"] = carr_menu
        return context

class CrearBlog(LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    model = Blog
    login_url = '/usuarios/login/'
    form_class = BlogForm
    template_name = 'crear_blog.html'
    permission_required = 'Blog.add_blog'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        carr_menu = Carrera.objects.all()
        context = super(CrearBlog, self).get_context_data(*args, **kwargs)
        context["carr_menu"] = carr_menu
        return context


class CrearCarrera(LoginRequiredMixin, CreateView):
    model = Carrera
    #form_class = BlogForm
    login_url = '/usuarios/login/'
    template_name = 'crear_carrera.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class EditarBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogEditForm
    login_url = '/usuarios/login/'
    template_name = 'editar_blog.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        carr_menu = Carrera.objects.all()
        context = super(EditarBlog, self).get_context_data(*args, **kwargs)
        context["carr_menu"] = carr_menu
        return context

class BorrarBlog(LoginRequiredMixin ,DeleteView):
    model = Blog
    login_url = '/usuarios/login/'
    template_name = 'borrar_blog.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        carr_menu = Carrera.objects.all()
        context = super(BorrarBlog, self).get_context_data(*args, **kwargs)
        context["carr_menu"] = carr_menu
        return context

class Comentar(LoginRequiredMixin, CreateView):
    model = Comentario
    login_url = '/usuarios/login/'
    form_class = ComentarioForm
    template_name = 'comentar.html'
 
    #OBTENER PK DE LA NOTICIA ORIGINAL
    def get_success_url(self):
        #Para hacer la redireccion al momento de comentar una noticia nececitamos el metodo para obtener la PK de la noticia asociada
        blog=self.kwargs['pk']
        return reverse_lazy('blog_detalle', kwargs={'pk': blog})


    #Hay que asociar el comentario a una noticia por su pk
    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['pk'] #obtener la pk de la notiias
        return super().form_valid(form)