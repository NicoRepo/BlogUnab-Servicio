from django.urls import path
#from Blog.views import 
from . import views

urlpatterns = [
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
  path('calendar', views.home, name='calendar'),
  path('callback', views.callback, name='callback'),
]