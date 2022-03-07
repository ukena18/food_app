# function api view
from rest_framework.decorators import api_view
# response json
from rest_framework.response import Response
# all the models
from base.models import Cook, Person, Food, Location, Cart, FoodOrder, Message, Comment
# all the serializers from serializers.py
from .serializer import LocationSerializer, \
    CookSerializer, PersonSerializer, CartSerializer, \
    FoodSerializer, FoodOrderSerializer, MessageSerializer, \
    CommentSerializer


@api_view(['GET', 'POST'])
def apiOverview(request):
    apis = {"location crud": [
        "path('locations/', name ='locations_api')",
        "path('location/<int:pk>', name ='location_api')"],

        "cook crud": [
            "path('cooks/',  name ='cooks_api')",
            "path('cook/<int:pk>', name ='cook_api')"],

        "person crud": [
            "path('persons/', name ='persons_api')",
            "path('person/<int:pk>', name ='person_api')"],

        "cart crud": [
            "path('carts/',name='carts_api')",
            "path('cart/<int:pk>', name='cart_api')"],

        "customer_sel_buy":
            "path('food_buy/person/<int:pk>/food/<int:fk>', name='food_buy')",

        "process the cart":
            "path('process/<int:pk>/', name='order_process')",

        "location pick so you can see all the foods":
            "path('location_pick/<int:pk>/', name='location_pick')",

        "based on user location pick the location":
            "path('user_location_pick/<int:pk>/', name='user_location_pick')",

        "food search":
            "path('food_search/<int:pk>/<str:food_str>/', name='food_search')",

        "comment_food":
            "path('comment_food/<int:pk>/', name='comment_food')",
        "Messages of the cook":
            "path('cook_msgs/<int:pk>/', name = 'cook_msgs')", }

    return Response(apis)


# api for custumor can buy and sell
# pk is for person and fk is for food you aregonna buy
@api_view(['GET', 'POST'])
def customer_buy_sell(request, pk, fk):
    # find the person
    # next phase it is gonna be auto
    person = Person.objects.get(pk=pk)
    # find the  food you want to add to cart
    food = Food.objects.get(pk=fk)
    # print(food)
    # print(person)
    # if the food amount more than 0 you can still buy amount you want
    if food.amount > 0:
        # if person already have the cart
        if person.cart_set.exists():
            # first try to get the cart
            # the only cart should be available the one process is false
            # because when you create or add it shouldn't have proceeded
            try:
                cart = person.cart_set.get(process=False)
            # if there are carts and all of them has been proceeded then create one with process = False
            except:
                cart = Cart.objects.create(process=False, person=person)
            # if the food is already has foodorder just increase the amount
            try:
                # every time you call the api it adds one more amount to foodorder amount
                # and took 1 from the food
                food_order = cart.foodorder_set.get(food__id=food.id)
                food_order.amount += 1

                food.amount -= 1
                food.save()
                food_order.save()
            # if not create food order with that food
            # and attach it to the cart
            except:
                food_order = FoodOrder.objects.create(food=food, cart=cart)
        # if there is no cart just create new one
        elif not person.cart_set.exists():
            # create a cart with person we passed it
            cart = Cart.objects.create(process=False, person=person)
            # create foodorder with cart and food
            food_order = FoodOrder.objects.create(food=food, cart=cart)
        serializer = FoodOrderSerializer(food_order)
        return Response(serializer.data)
    elif food.amount <= 0:
        return Response({"error": "there is no food left sorry"})


@api_view(['GET', 'POST'])
# this is for processing the order
# find the person, so we can check the latest order he has
def order_process(request, pk):
    person = Person.objects.get(pk=pk)
    # if person has the cart find this person cart
    if person.cart_set.exists():
        try:
            cart = person.cart_set.get(process=False)
        except:
            return Response({"error": "you are already proceed the cart"})
        # proceeded the cart
        cart.process = True
        # get all the food orders from cart to send to cook
        food_orders = cart.foodorder_set.all()
        # loop through the food_orders
        for food_order in food_orders:
            # find the cook for each of those food_order
            cook = food_order.food.cook
            # create  the message model for each  food_order
            msg = f'you have got an order from {person.first_name} .' \
                  f' The food is {food_order.food.name} x {food_order.amount} '
            sent_msg = Message(msg_from=person, msg_to=cook, msg=msg, order=food_order)
            # save all the messages
            sent_msg.save()
        # save the cart as done
        cart.save()
        return Response({"success": "your order has been placed The Cook is already got the message "})


# find all the food based on the location
@api_view(['POST', 'GET'])
def location_pick(request, pk):
    # get the locs
    loc = Location.objects.get(pk=pk)
    # filter through the cooks who have loc as location
    cooks = Cook.objects.filter(location=loc)
    # create an empty foods array then we are going to append all the food WE HAVE
    foods = []
    # loop through the cooks
    for cook in cooks:
        # get the foods of all the cook
        for food in cook.food_set.all():
            # add food the foods array
            foods.append(food)
    # print(foods)
    # create a serializer spo you can display them
    serializer = FoodSerializer(foods, many=True)
    # print(cooks)
    # display them
    return Response(serializer.data)


# all the available foods for the users locations
# get the all food based on user location
@api_view(['POST', 'GET'])
def user_location_pick(request, pk):
    #  find the person
    person = Person.objects.get(pk=pk)
    # find the loc
    loc = person.location
    #  find the cook matching with location
    cooks = Cook.objects.filter(location=loc)
    foods = []
    #  loop through the cooks and food they made
    for cook in cooks:
        for food in cook.food_set.all():
            foods.append(food)
    print(foods)
    # call foodSerializer
    serializer = FoodSerializer(foods, many=True)
    # print(cooks)
    # display the as a Json
    return Response(serializer.data)


# search for food based on user location
@api_view(['POST', 'GET'])
def food_search(request, pk, food_str):
    # find the user
    person = Person.objects.get(pk=pk)
    # find the LOC
    loc = person.location
    # find the Cook who share the same loc
    cooks = Cook.objects.filter(location=loc)

    foods = []
    for cook in cooks:
        # from every cook get the food contain food_str
        for food in cook.food_set.filter(name__icontains=food_str):
            foods.append(food)
    print(foods)
    serializer = FoodSerializer(foods, many=True)
    # print(cooks)
    return Response(serializer.data)


# if you bought the food you can comment about it
@api_view(['GET', 'POST'])
def comment_food(request, pk):
    # find the user
    person = Person.objects.get(pk=pk)
    # find all the food_orders
    foodorders = [cart.foodorder_set.all() for cart in person.cart_set.all()]
    foods = []
    # loop through of all the food_orders
    for foodorder_query in foodorders:
        # loop through of all the food_orders
        for foodorder in foodorder_query:
            # get the foods you have been ordered
            foods.append(foodorder.food)
    # serializer = CartSerializer(carts, many=True)
    # return Response(serializer.data)
    # print(foodorders)
    # get all the food's name
    foods = [i.name for i in foods]
    # print(foods)
    #  if it is post method then get the data
    if request.method == 'POST':
        # if the food name is in our pre-ordered place we have right to order them
        if request.data["food"] in foods:
            # create the comment based on data we get

            comment = Comment.objects.create(person=person, text=request.data['text'],
                                             food=Food.objects.get(name=request.data["food"]))
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
    # change that to all the comment about the food
    return Response("success")


@api_view(['GET', 'POST'])
def cook_msgs(request, pk):
    cook = Cook.objects.get(pk=pk)
    msgs = cook.message_set.all()
    print(msgs)
    serializer = MessageSerializer(msgs, many=True)
    return Response(serializer.data)
