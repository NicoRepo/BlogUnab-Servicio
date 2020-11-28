from django import forms
from .models import Blog, Carrera, Comentario

carreras = Carrera.objects.all().values_list('nombre','nombre')
eleccion = []
for carrera in carreras:
    eleccion.append(carrera)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('titulo','autor_id','carrera','cuerpo')
        

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la Noticia' }),
            #'autor_id': forms.Select(attrs={'class': 'form-control' }),
            'autor_id': forms.TextInput(attrs={'class': 'form-control','value':'' ,'id':'user', 'type':'hidden'}),
            'carrera': forms.Select(choices=eleccion, attrs={'class': 'form-control' }),
            'cuerpo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cuerpo de la Noticia'}),
        }

class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('titulo','carrera','cuerpo')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo de la Noticia' }),
            'carrera': forms.Select(choices=eleccion, attrs={'class': 'form-control' }),
            'cuerpo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cuerpo de la Noticia'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields  = ('nombre', 'cuerpo')

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','value':'' ,'id':'nombre', 'type':'hidden'}),
            'cuerpo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe algo...'}),
        }