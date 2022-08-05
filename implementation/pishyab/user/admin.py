from django.contrib import admin
from .models import MyUser

admin.site.register(MyUser)
admin.site.login_template = "user/admin/accounts/login_temp.html"