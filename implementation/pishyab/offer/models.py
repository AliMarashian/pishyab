from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    percentage = models.IntegerField()