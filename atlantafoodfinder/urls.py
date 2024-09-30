# atlantafoodfinder/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include users app URLs
    path('restaurants/', include('restaurants.urls')),  # Include restaurants app URLs here
    path('', views.home, name='home'),  # Use the home view from restaurants as root path
    path('search/', views.search_results, name='search_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
