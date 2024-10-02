from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('restaurant/<str:place_id>/', views.restaurant_detail, name='restaurant_detail'),  # Restaurant detail by place_id
    path('cuisines/', views.cuisine_list, name='cuisine_list'),  # List of all cuisines
    path('cuisine/<int:cuisine_id>/', views.restaurant_by_cuisine, name='restaurant_by_cuisine'),  # Restaurants by cuisine
    path('restaurant/<int:pk>/add_review/', views.add_review, name='add_review'),  # Add review
    path('restaurant/<int:pk>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),  # Toggle favorite
    path('api/restaurants/', views.restaurant_api, name='restaurant_api'),  # API endpoint for restaurants
    path('restaurants/', views.restaurant_list, name='restaurant_list'),  # List of all restaurants
    
    # Use only **one** of these search paths
    path('search/', views.search_results, name='search_results'),  # Search results page
]
