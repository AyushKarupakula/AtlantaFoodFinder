from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')