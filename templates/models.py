from django.db import models
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
    size = models.CharField(max_length=10)

class PizzaCrust(models.Model):
    crust = models.CharField(max_length=10)

class PizzaCheese(models.Model):
    cheese = models.CharField(max_length=10)

class PizzaSauce(models.Model):
    sauce = models.CharField(max_length=10)

##### Grabbing all available items from our database
items = PizzaSizes.objects.all()
pizzaSizes = tuple((size.size, size.size) for size in items)

items = PizzaCrust.objects.all()
pizzaCrustSize = tuple((item.crust, item.crust) for item in items)

items = PizzaSauce.objects.all()
pizzaSauce = tuple((item.sauce, item.sauce) for item in items)

items = PizzaCheese.objects.all()
pizzaCheese = tuple((item.cheese, item.cheese) for item in items)

# print(pizzaCheese)

#### Pizza Topping Config /////////////// No longer used

######################## PIZZA MODEL
class Pizza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=pizzaSizes, default='medium')
    crust = models.CharField(max_length=15, choices=pizzaCrustSize, default='normal')
    sauce = models.CharField(max_length=10, choices=pizzaSauce, default='tomato')
    cheese = models.CharField(max_length=10, choices=pizzaCheese, default='mozzarella')

    # pepporoni = models.CharField(max_length=10, choices=pepporoni, default="none")
    # chicken = models.CharField(max_length=10, choices=chicken, default="none")
    # ham = models.CharField(max_length=10, choices=ham, default="none")
    # pineapple = models.CharField(max_length=10, choices=pineapple, default="none")
    # mushrooms = models.CharField(max_length=10, choices=mushrooms, default="none")
    # onions = models.CharField(max_length=10, choices=onions, default="none")
    # peppers = models.CharField(max_length=10, choices=peppers, default="none")

    toppings = models.CharField(max_length=500)

    date = models.DateTimeField(auto_now_add=True, blank=True)

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

class Delivery(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cardNo = models.IntegerField()
    expMonth = models.CharField(max_length=15, choices=month, default='January')
    expYear = models.IntegerField()
    cvv = models.IntegerField(max_length=4)
