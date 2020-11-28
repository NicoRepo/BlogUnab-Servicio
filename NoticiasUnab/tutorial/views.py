from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from tutorial.auth_helper import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_token
from tutorial.graph_helper import get_user

def home(request):
  context = initialize_context(request)

  return render(request, 'tutorial/home.html', context)

def initialize_context(request):
  context = {}

  # Check for any errors in the session
  error = request.session.pop('flash_error', None)

  if error != None:
    context['errors'] = []
    context['errors'].append(error)

  # Check for user in the session
  context['user'] = request.session.get('user', {'is_authenticated': False})
  return context

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect(reverse('home'))

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)
  # Get the user's profile
  user = get_user(token)

  # Get user info
  # user attribute like displayName,surname,mail etc. are defined by the 
  # institute incase you are using single-tenant. You can get these 
  # attribute by exploring Microsoft graph-explorer.

  fullname = user['displayName']
  split_name = fullname.split(' ')
  first_name = split_name[2]
  last_name = split_name[0]
  first_name = first_name.lower().title()
  last_name = last_name.lower().title()


  username = user['displayName']
  password = user['surname']
  email = user['mail']

  try:
      # if use already exist
      user = User.objects.get(username=username)

  except User.DoesNotExist:
      # if user does not exist then create a new user
      user = User.objects.create_user(username,email,password)
      user.first_name = first_name
      user.last_name = last_name
      user.save()

  user = authenticate(username=username,password=password)

  if user is not None:
      login(request,user)
      messages.success(request,"Success: You were successfully logged in.")
      return redirect('home')
  return redirect('home')
