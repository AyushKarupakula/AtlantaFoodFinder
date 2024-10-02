# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin  # For requiring login in class-based views

from restaurants.models import Favorite
from django.views.generic import View


# Sign Up View using CustomUserCreationForm
class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm  # Use your custom form here
    success_url = '/'  # Redirect to home after successful signup

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after signup
        return redirect(self.success_url)  # Redirect to homepage


# Login View using AuthenticationForm
class LoginUserView(LoginView):
    print("hello")
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'  # Redirect to homepage after successful login

    def get_success_url(self):
        return self.success_url


# Dashboard View - Only accessible to logged-in users
class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'dashboard.html'
    login_url = 'login'  # Redirects to login if not authenticated
    context_object_name = 'favorites'
    
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)


# Logout View with a confirmation page
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    http_method_names = ['post']
    template_name = 'users/logout.html'
    next_page = 'login'



# Profile View requiring login
@login_required
def profile(request):
    return render(request, 'users/profile.html')
