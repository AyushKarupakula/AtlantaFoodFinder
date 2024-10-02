# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Custom logout view
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),  # Dashboard view
    path('profile/', views.profile, name='profile'),  # Profile view

]
