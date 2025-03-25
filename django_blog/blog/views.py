from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_view = 'blog/templates/blog/register.html'

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to the profile page after login
        else:
            messages.error(request, 'Invalid username or password')  # Add error message
    return render(request, 'blog/login.html')

from django.shortcuts import redirect
from django.contrib.auth import logout

def custom_logout_view(request):
    logout(request)  # Logs out the user
    return redirect('/')





# Create your views here.
