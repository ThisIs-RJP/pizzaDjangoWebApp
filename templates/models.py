from django.db import models

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
