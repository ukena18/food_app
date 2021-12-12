from django.shortcuts import render
from .models import Food, Buyer, Seller
from django.contrib.auth.models import User
from .forms import SellerForm, FoodForm, BuyerForm


def food(request):
    food_form = FoodForm()


    if request.method=="POST":
        print(request.POST)
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()



    context = {"food_form":food_form}
    return render(request, "base/food.html", context)



def seller(request):
    form = SellerForm()
    if request.method == "POST":
        user_id = request.POST.get("user")
        user = User.objects.get(id=user_id)

        seller = Seller(user=user)
        seller.save()
    context = {"form":form}
    return render(request, "base/seller.html", context)



def buyer(request):
    buyer_form = BuyerForm()

    if request.method=="POST":
        print(request.POST)

    context = {"buyer_form":buyer_form }
    return render(request, "base/buyer.html", context)