from django.db import models
from django.contrib.auth.models import User

######################## PIZZA CONFIG 

pizzaSizes = (
    ("small", "small"),
    ("medium", "medium"),
    ("large", "large"),
)

pizzaCrustSize = (
    ("thin", "thin"),
    ("normal", "normal"),
    ("thick", "thick"),
    ("gluten free", "gluten free"),
)

pizzaSauce = (
    ("tomato", "tomato"),
    ("vegan", "bbq"),
)

pizzaCheese = (
    ("mozzarella", "mozzarella"),
    ("vegan", "vegan"),
    ("low fat", "low fat"),
)

#### Pizza Topping Config

pepporoni = (
    ("none", "none"),
    ("pepporoni", "pepporoni"),
)

chicken = (
    ("none", "none"),
    ("chicken", "chicken"),
)

ham = (
    ("none", "none"),
    ("ham", "ham"),
)


pineapple = (
    ("none", "none"),
    ("pineapple", "pineapple"),
)


mushrooms = (
    ("none", "none"),
    ("mushrooms", "mushrooms"),
)


onions = (
    ("none", "none"),
    ("onions", "onions"),
)

peppers = (
    ("none", "none"),
    ("peppers", "peppers"),
)

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
    cardNo = models.IntegerField(max_length=20)
    expMonth = models.CharField(max_length=15, choices=month, default='January')
    expYear = models.IntegerField(max_length=4)
    cvv = models.IntegerField(max_length=4)
