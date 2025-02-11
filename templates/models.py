from django.db                  import models
from django.contrib.auth.models import User

######################## PIZZA CONFIG 

# pizzaSizes = (
#     ("small", "small"),
#     ("medium", "medium"),
#     ("large", "large"),
# )

# pizzaCrustSize = (
#     ("thin", "thin"),
#     ("normal", "normal"),
#     ("thick", "thick"),
#     ("gluten free", "gluten free"),
# )

# pizzaSauce = (
#     ("tomato", "tomato"),
#     ("vegan", "bbq"),
# )

# pizzaCheese = (
#     ("mozzarella", "mozzarella"),
#     ("vegan", "vegan"),
#     ("low fat", "low fat"),
# )

class PizzaSizes(models.Model):
    size = models.CharField(max_length=20)

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=20)

class PizzaCheese(models.Model):
    cheese = models.CharField(max_length=20)

class PizzaSauce(models.Model):
    sauce = models.CharField(max_length=20)

##### Grabbing all available items from our database

items       = PizzaSizes.objects.all()
pizza_sizes = tuple((size.size, size.size) for size in items)

items            = PizzaCrust.objects.all()
pizza_crist_size = tuple((item.crust, item.crust) for item in items)

items       = PizzaSauce.objects.all()
pizza_sauce = tuple((item.sauce, item.sauce) for item in items)

items        = PizzaCheese.objects.all()
pizza_cheese = tuple((item.cheese, item.cheese) for item in items)

# print(pizza_cheese)

#### Pizza Topping Config /////////////// No longer used

######################## PIZZA MODEL

class Pizza(models.Model):
    author   = models.ForeignKey(User, on_delete=models.CASCADE)
    size     = models.CharField(max_length=20, choices=pizza_sizes,      default='medium')
    crust    = models.CharField(max_length=20, choices=pizza_crist_size, default='normal')
    sauce    = models.CharField(max_length=20, choices=pizza_sauce,      default='tomato')
    cheese   = models.CharField(max_length=20, choices=pizza_cheese,     default='mozzarella')
    toppings = models.CharField(max_length=500)
    date     = models.DateTimeField(auto_now_add=True,                   blank=True)

############# Delivery Config

month = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

years = tuple((year, year) for year in range(2022, 2050))

class Delivery(models.Model):
    author   = models.ForeignKey(User, on_delete=models.CASCADE)
    name     = models.CharField(max_length=100)
    address  = models.CharField(max_length=200)
    cardNo   = models.IntegerField()
    expMonth = models.CharField(max_length=15,    choices=month, default='January')
    expYear  = models.IntegerField(choices=years, default=2000)
    cvv      = models.IntegerField(max_length=4)
