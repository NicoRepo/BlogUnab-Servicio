from django.urls import path
from .views import RegistrarUsuario
from django.contrib.auth import views
from .forms import UserLoginForm

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),
    path(
        'login/',
        views.LoginView.as_view(
            template_name="login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
)
    
]
