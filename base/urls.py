from django.urls import path, include
from . import views

urlpatterns = [
    path("food/",views.food,name="food"),
    path("",views.food,name="food"),
    path("seller/",views.seller,name="seller"),
    path("buyer/",views.buyer,name="buyer"),


]
