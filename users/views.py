from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'

@login_required
def profile(request):
    return render(request, 'profile.html')