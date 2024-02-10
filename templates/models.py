from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
