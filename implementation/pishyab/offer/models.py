from django.db import models
from django.contrib.auth.models import User




class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    priority = models.IntegerField(default=1)
    pic_link = models.CharField(max_length = 400, default="https://www.citypng.com/public/uploads/preview/warranty-ribbon-blue-icon-logo-sign-label-badge-png-11635941164yp8i70hmcb.png")