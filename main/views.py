from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, View
from django.conf import settings
from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from .models import Department
from .forms import DepartmentForm
# Create your views here.

class Index(TemplateView):
   template_name = 'main/index.html'

class Register (CreateView):
    model = settings.AUTH_USER_MODEL
    form_class  = RegistrationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:login')

class Login_View(LoginView):
    model = settings.AUTH_USER_MODEL
    form_class = LoginForm
    template_name = 'main/signin.html'

    def get_success_url(self):
        url = reverse_lazy('dashboard:index')
        return url

class Logout_View(View):
    def get(self,request):
        logout(self.request)
        return redirect('main:login',permanent=True)
