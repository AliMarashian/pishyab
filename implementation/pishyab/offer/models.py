from django.db import models
from django.contrib.auth.models import User




class Offer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    price = models.IntegerField()
    discount = models.IntegerField()