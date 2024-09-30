from django.contrib.auth.models import AbstractUser
from django.db import models
from restaurants.models import Restaurant
from django.conf import settings

class CustomUser(AbstractUser):
    # Add any additional fields here
    pass

class UserFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
