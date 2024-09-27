from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('cuisines/', views.cuisine_list, name='cuisine_list'),
    path('cuisine/<int:cuisine_id>/', views.restaurant_by_cuisine, name='restaurant_by_cuisine'),
    path('restaurant/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('restaurant/<int:pk>/toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('api/restaurants/', views.restaurant_api, name='restaurant_api'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
]