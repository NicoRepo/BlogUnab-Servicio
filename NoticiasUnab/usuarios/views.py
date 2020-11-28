from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegistroUser
from django.contrib.auth.models import User

class RegistrarUsuario(generic.CreateView):
    model = User
    form_class = RegistroUser
    template_name = 'registration/registrarse.html'
    success_url = reverse_lazy('login')


