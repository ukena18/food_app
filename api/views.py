# function api view
from rest_framework.decorators import api_view
# response json
from rest_framework.response import Response
# all the models
from base.models import Cook,Person,Food, Location, Cart
# all the serializers from serializers.py
from .serializer import LocationSerializer, \
    CookSerializer, PersonSerializer, CartSerializer


##########
########
###   when you want to create remove id
### and if there is an array remove all unused commas (,)

#  all the crud operation for location
@api_view(['GET', 'POST'])
def locations_api(request):
    # get all the locations
    if request.method == 'GET':
        locs = Location.objects.all()
        # serialize the model
        # many=True means more than one queryset
        serializer = LocationSerializer(locs, many=True)
        # return the jsno response
        return Response(serializer.data)

    # if it is post then create new location
    elif request.method == 'POST':
        # get the request.data and put inside serializer
        serializer = LocationSerializer(data=request.data)
        # if location serializer is valid
        if serializer.is_valid():
            #then save it
            serializer.save()
            # send the new thing as a REsponse
            return Response(serializer.data)
        # if there is mistake show the errror
        return Response(serializer.errors)
# detail and update
@api_view(['GET', 'POST'])
# pk is for detail and update
def location_api(request,pk):
    if request.method == 'GET':
        #get the single loc for detail view
        loc = Location.objects.get(pk=pk)
        serializer = LocationSerializer(loc)
        return Response(serializer.data)

    # if it post the update the instance
    elif request.method == 'POST':
        # find the loc
        loc = Location.objects.get(pk=pk)
        # get the data  from request.data
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            # the way we update first instance we wanna update
            # then the validated_data we  will update
            serializer.update(instance=loc,validated_data=serializer.data)
            # return json response
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def cooks_api(request):
    if request.method == 'GET':
        cooks = Cook.objects.all()
        serializer = CookSerializer(cooks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def cook_api(request,pk):
    if request.method == 'GET':
        cook = Cook.objects.get(pk=pk)
        serializer = CookSerializer(cook)
        return Response(serializer.data)

    elif request.method == 'POST':
        cook = Cook.objects.get(pk=pk)
        serializer = CookSerializer(data=request.data)

        if serializer.is_valid():
            # get the loc var from request.data
            lk = request.data['location']
            # find the location from database
            location = Location.objects.get(pk=lk)
            # change cook.location to our location
            cook.location = location
            # save it to the db
            cook.save()
            # then with using db update it
            serializer.update(instance=cook, validated_data=serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def persons_api(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def person_api(request,pk):
    if request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'POST':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            lk = request.data['location']
            location = Location.objects.get(pk=lk)
            person.location = location
            person.save()
            serializer.update(instance=person, validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'POST'])
def carts_api(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST'])
def cart_api(request,pk):
    if request.method == 'GET':
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    elif request.method == 'POST':
        cart = Cart.objects.get(pk=pk)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(instance=cart, validated_data=request.data)
            return Response(serializer.data)
        return Response(serializer.errors)

