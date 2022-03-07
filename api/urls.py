from django.urls import path
from . import views
from . import views_func

urlpatterns = [

    path('', views_func.apiOverview, name='apiOveriew'),
    # location crud
    path('locations/', views.locations_api, name ='locations_api'),
    path('location/<int:pk>', views.location_api, name ='location_api'),

    # cook crud
    path('cooks/', views.cooks_api, name ='cooks_api'),
    path('cook/<int:pk>', views.cook_api, name ='cook_api'),

    # person crud
    path('persons/', views.persons_api, name ='persons_api'),
    path('person/<int:pk>', views.person_api, name ='person_api'),

    # cart crud
    path('carts/', views.carts_api, name='carts_api'),
    path('cart/<int:pk>', views.cart_api, name='cart_api'),

    # customer_sel_buy
    path('food_buy/person/<int:pk>/food/<int:fk>', views_func.customer_buy_sell, name='food_buy'),
    # process the cart
    path('process/<int:pk>/', views_func.order_process, name='order_process'),
    #location pick so you can see all the foods
    path('location_pick/<int:pk>/', views_func.location_pick, name='location_pick'),
    # based on user location pick the location
    path('user_location_pick/<int:pk>/', views_func.user_location_pick, name='user_location_pick'),
    # food search
    path('food_search/<int:pk>/<str:food_str>/', views_func.food_search, name='food_search'),
    #comment_food
    path('comment_food/<int:pk>/', views_func.comment_food, name='comment_food'),
    # Messagges of the cook
    path("cook_msgs/<int:pk>/", views_func.cook_msgs, name = 'cook_msgs'),

]
