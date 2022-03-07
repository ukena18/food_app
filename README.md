# noza_Eats



** in order to run code **

install python 10.0.0 or higher
create virtual enviroment (optinal)
open the project folder which manage.py located
open terminal
if you created virtual env activate if not just skipt this part
run pip install -r requirements.txt


How to PArt1



- First lets create 3 users
- add more than 2 locations .
```python
##path('locations/', views.locations_api, name ='locations_api'),
```
- then create 1 cook and 1 person
```python
##path('cooks/', views.cooks_api, name ='cooks_api'),
##path('persons/', views.persons_api, name ='persons_api'),
```
- create more than 3 food with cook

-create a cart for a person
```python
##path('cart/<int:pk>', views.cart_api, name='cart_api'),
```
- let the person foodorder and add to cart
```python
##path('food_buy/person/<int:pk>/food/<int:fk>', views_func.customer_buy_sell, name='food_buy'),
```
- process the cart
```python
##path('process/<int:pk>/', views_func.order_process, name='order_process'),
```
- then check cook msgs
```python
##    path("cook_msgs/<int:pk>/", views_func.cook_msgs, name = 'cook_msgs'),
```
