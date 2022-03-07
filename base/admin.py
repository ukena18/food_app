from django.contrib import admin
from .models import Food,Comment,Location,Cook, Cart, Person, FoodOrder, Message



admin.site.register(Food)
admin.site.register(Message)
admin.site.register(FoodOrder)
admin.site.register(Comment)
admin.site.register(Cook)
admin.site.register(Location)
admin.site.register(Cart)
admin.site.register(Person)


