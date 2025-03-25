from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_view = 'blog/templates/blog/register.html'

class LogoutView(TemplateView):
    success_url = reverse_lazy('logout')
    template_view = 'blog/templates/blog/logout.html'

class LoginView(TemplateView):
    success_url = reverse_lazy('login')
    template_view = 'blog/templates/blog/login.html'





# Create your views here.
