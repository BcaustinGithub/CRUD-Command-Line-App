from django.db import models

class Contact(models.Model):
    make = models.TextField()
    model = models.TextField()
    miles = models.IntegerField()
    year = models. IntegerField()
    price = models.IntegerField()


def create_car():
    ...

def remove_car():
    ...

def sell_car():
    ...

def profits():
    ...

def price_calculator():
    ...