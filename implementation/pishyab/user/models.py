from django.db import models
from django import forms
from django.contrib.auth.models import User
from offer.models import Offer

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_provider = models.BooleanField()
    phone_no = models.CharField(max_length = 20)
    orgname = models.CharField(max_length = 50, null=True)
    address = models.CharField(max_length = 100, null=True)
    description = models.CharField(max_length = 200, null=True)
    fav_offers = models.ManyToManyField(Offer)