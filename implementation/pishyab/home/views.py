from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from user.models import MyUser
from django.contrib.auth.models import User


def index(request):
    username = request.session.get("username")
    # user = User(email="salam")
    # user.save()
    # print(user)
    # print(User.objects.get(id="1").orgname)
    if username != None:
        user = User.objects.get(username=username)
        my_user = MyUser.objects.get(user=user)
    return render(request, 'home/index.html', {'title':'پیشیاب', 'my_user':my_user})