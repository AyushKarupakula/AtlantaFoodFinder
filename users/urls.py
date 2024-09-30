from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard')
    # path('search/', views.search, name="search"),
]