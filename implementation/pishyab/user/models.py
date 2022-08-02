from django.db import models
from django import forms
from django.contrib.auth.models import User
from offer.models import Offer

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_provider = models.BooleanField()
    phone_no = models.CharField(max_length = 20)
    pic_link = models.CharField(max_length = 400, default="https://www.citypng.com/public/uploads/preview/warranty-ribbon-blue-icon-logo-sign-label-badge-png-11635941164yp8i70hmcb.png")
    fav_offers = models.ManyToManyField(Offer)

    orgname = models.CharField(max_length = 50, null=True)
    address = models.CharField(max_length = 100, null=True)
    description = models.CharField(max_length = 200, null=True)
    license_link = models.CharField(max_length = 400, null=True)
    is_verified = models.BooleanField(default=False)