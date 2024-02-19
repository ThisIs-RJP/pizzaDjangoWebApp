from django.db import models
from django.contrib.auth.models import User

# COLOR_CHOICES = (
#     ('green','GREEN'),
#     ('blue', 'BLUE'),
#     ('red','RED'),
#     ('orange','ORANGE'),
#     ('black','BLACK'),
# )

# class MyModel(models.Model):
#   color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')


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

######################## PIZZA MODEL

class Pizza(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=pizzaSizes, default='medium')
    crust = models.CharField(max_length=15, choices=pizzaCrustSize, default='normal')
    sauce = models.CharField(max_length=10, choices=pizzaSauce, default='tomato')
    cheese = models.CharField(max_length=10, choices=pizzaCheese, default='mozzarella')