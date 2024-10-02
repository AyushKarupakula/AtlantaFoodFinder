# restaurants/admin.py
from django.contrib import admin
from .models import Restaurant, Cuisine, Review

admin.site.register(Restaurant)
admin.site.register(Cuisine)
admin.site.register(Review)
