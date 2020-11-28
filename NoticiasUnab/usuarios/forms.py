from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroUser(UserCreationForm):
    
    class Meta:
        model = User
        fields = [ 'username', 'first_name' , 'last_name', 'email' ,'password1', 'password2']

        widgets = {
            'Nombre de Usuario:': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario' }),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre' }),
            'Apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido' }),
            'Correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo' }),
            'Password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña' }),
            'ConfirmaPassword': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña' }),
        }

        labels = {
            'Nombre de Usuario:': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario' }),
            'Nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre' }),
            'Apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido' }),
            'Correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Correo' }),
            'Password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña' }),
            'ConfirmaPassword': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Contraseña' }),
        }        

class UserLoginForm(AuthenticationForm):
    def init(self, args, **kwargs):
        super(UserLoginForm, self).init(args, **kwargs)
    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))