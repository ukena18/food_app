# get the serializers from rest_framework
from rest_framework import serializers
# Get all the model for turn into serializers
from base.models import Food, Cook, Person, Cart,\
    Comment, Location, FoodOrder, Message


# Food Model to serializers
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


# Location Model to serializers
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


# Cook Model to serializers
class CookSerializer(serializers.ModelSerializer):
    # when we send and get cook as an json
    # read_only means you can't change it but we will use some signals to change it
    location = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cook
        # all the models instances except cook
        exclude = ["cook"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    # when we send and get cook as an json
    # get emphasise that location is foreignKey
    # read_only means you can't change it but we will use some signals to change it
    location = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Person
        exclude = ['person']

    # overwrite the update for PErsonSerializer
    # add all the cats to the person model
    def update(self, validated_data, instance):
        carts = validated_data.pop("carts")
        # clear the m2m relation with carts empty the array
        instance.carts.clear()
        print(carts)
        for i in carts:
            # add the array one by one
            cart = Cart.objects.get(pk=int(i))
            instance.carts.add(cart)
        instance.save()


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

        def update(self, validated_data, instance):
            foods = validated_data.pop("foods")
            # clear the m2m relation with carts empty the array
            instance.food.clear()
            print(foods)
            for i in foods:
                # add the array one by one
                food = Food.objects.get(pk=int(i))
                instance.foods.add(food)
            instance.save()


class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOrder
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

