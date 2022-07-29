from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from user.models import MyUser
from offer.models import Offer
from django.contrib.auth.models import User


def index(request):
    username = request.session.get("username")
    all_offers = Offer.objects.all().values()

    for offer in all_offers:
        initial_user = User.objects.get(id = offer['user_id'])
        my_user = MyUser.objects.get(user = initial_user)
        offer['orgname'] = my_user.orgname
        offer['username'] = initial_user.username

    # return render(request, "offer/view_offers.html", context)
    myuser = None
    if username != None:
        user = User.objects.get(username=username)
        myuser = MyUser.objects.get(user=user)
    return render(request, 'home/index.html', {'title':'پیشیاب', 'myuser':myuser, 'myoffers': all_offers})