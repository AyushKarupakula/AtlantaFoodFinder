from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurants.urls')),
    path('users/', include('users.urls')),
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)