from django.db import models
from django.conf import settings

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='restaurant_images', blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review for {self.restaurant.name}"