from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Location(models.Model):
    location = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.location


class Person(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name

class Cook(models.Model):
    cook = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.first_name



class Food(models.Model):
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    expire = models.DateTimeField(default=timezone.now, null=True, blank=True)
    amount = models.IntegerField(default=1, null=True, blank=True)
    cost = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    process = models.BooleanField(default=False,null=True,blank=True)
    transaction_id = models.IntegerField(default=0, null=True, blank=True, unique=True)
    def __str__(self):
        return str(self.id)

class FoodOrder(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(default=1, null=True, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'food order {self.id} ---> {self.food.name} to {self.cart.id}'


class Comment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text[0:50]

class Message(models.Model):
    msg_from = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
    msg_to = models.ForeignKey(Cook, on_delete=models.CASCADE, null=True, blank=True)
    msg = models.TextField(null=True, blank=True)
    order =  models.ForeignKey(FoodOrder, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.msg[:20]


