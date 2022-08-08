from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from user.models import MyUser
from offer.models import Offer
from django.contrib.auth.models import User
import geopy.distance


def distance(loc1, loc2):
    loc1_ = list(map(float, loc1.split(',')))
    loc2_ = list(map(float, loc2.split(',')))

    return geopy.distance.geodesic(loc1_, loc2_).km


def index(request):
    username = request.session.get("username")
    all_offers = Offer.objects.all().values()
    category_offers = {}
    if username != None and User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        myuser = MyUser.objects.get(user=user)
        dist = []
        for offer in all_offers:
            initial_user = User.objects.get(id=offer['user_id'])
            my_user = MyUser.objects.get(user=initial_user)
            dist.append(distance(myuser.location, my_user.location))

    sorted_offers = sorted(zip(all_offers, dist), key=lambda t: t[1])

    for offer, dist_ in sorted_offers:
        initial_user = User.objects.get(id = offer['user_id'])
        my_user = MyUser.objects.get(user = initial_user)
        offer['orgname'] = my_user.orgname
        offer['username'] = initial_user.username
        if not offer['category'] in category_offers:
                category_offers[offer['category']] = []
        category_offers[offer['category']].append((offer, dist_))

    # return render(request, "offer/view_offers.html", context)
    myuser = None
    if username != None and User.objects.filter(username = username).exists():
        user = User.objects.get(username=username)
        myuser = MyUser.objects.get(user=user)
        for offer in all_offers:
            offer['fav'] = myuser.fav_offers.filter(id=offer['id']).exists()
    return render(request, 'home/index.html', {'title':'پیشیاب', 'myuser':myuser, 'myoffers': all_offers, 'category_offers':category_offers})