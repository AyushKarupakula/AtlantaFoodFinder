from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    favorite_restaurants = models.ManyToManyField('restaurants.Restaurant', related_name='favorited_by')

    def __str__(self):
        return self.username