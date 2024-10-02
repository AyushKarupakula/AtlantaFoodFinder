# restaurants/admin.py
from django.contrib import admin
from .models import Restaurant, Cuisine, Review, Favorite


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_address', 'rating')
    search_fields = ('name', 'formatted_address')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Cuisine)
admin.site.register(Review)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'restaurant')  # Specify fields to display
    search_fields = ('user__username', 'restaurant__name')  # Add search functionality

admin.site.register(Favorite, FavoriteAdmin)
