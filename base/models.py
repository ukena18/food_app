from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

class Food(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    food_name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True)
    cost = models.IntegerField(null=True)



    def __str__(self):
        return self.food_name


class Buyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    food = models.ManyToManyField(Food, blank=True)

    def __str__(self):
        return self.user.username

