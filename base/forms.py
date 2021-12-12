from django import forms
from .models import Seller, Food, Buyer


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields= '__all__'


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = '__all__'