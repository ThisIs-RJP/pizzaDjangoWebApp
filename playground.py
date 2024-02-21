#!/usr/bin/env python3

cheeses = ["mozzarella", "vegan", "low fat"]
pizzaCheese = tuple((cheese, cheese) for cheese in cheeses)
print(pizzaCheese)