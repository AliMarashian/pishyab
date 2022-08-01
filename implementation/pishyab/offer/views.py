from django.shortcuts import render, redirect

from user.models import MyUser
from .forms import NewOfferForm
from django.contrib import messages
from .models import Offer
from django.contrib.auth.models import User
from django.db.models import Q




def new_offer(request):

    # Check if user is logged in as provider
    username = request.session.get("username")
    if username == None:
        return render(request, 'home/index.html', {'title':'پیشیاب'})

    user = User.objects.get(username=username)
    myuser = MyUser.objects.get(user=user)
    if not myuser.is_provider:
        return render(request, 'home/index.html', {'title':'پیشیاب', 'myuser':myuser})

    if request.method == 'POST':
        form = NewOfferForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            try:
                username = request.session.get("username")
                user = User.objects.get(username=username)
                print(username, user, user.email)
            except:
                print("ERROR | New_Offer | No User")
                return render(request, 'offer/new_offer.html', {'form': form, 'title':'پیشنهاد جدید'})

            print(user)
            new_offer = Offer(user=user, title=cleaned_form.get("title"), description=cleaned_form.get("description"), start_date=cleaned_form.get("start_date"), start_time=cleaned_form.get("start_time"),
                end_date=cleaned_form.get("end_date"), end_time=cleaned_form.get("end_time"), price=cleaned_form.get("price"), discount=cleaned_form.get("discount"))
            new_offer.save()

            return redirect('/set_offer_priority/'+str(new_offer.id))
    else:
        form = NewOfferForm()
    return render(request, 'offer/new_offer.html', {'form': form, 'title':'پیشنهاد جدید', 'myuser': myuser})
   


def view_offers(request):

    my_offers = Offer.objects.all().values()
    # template = loader.get_template('view_schedule.html')
    
    for offer in my_offers:
        # print(offer['title'])
        # print(User.objects.get(id = offer.user_id).username)
        offer['username'] = User.objects.get(id = offer['user_id']).username
    
    context = {
        'myoffers': my_offers,
    }

    print("*" * 100)
    return render(request, "offer/view_offers.html", context)



def search_offer(request, input_):
    username = request.session.get("username")
    all_offers = Offer.objects.filter(Q(title__icontains=input_) | Q(description__icontains=input_)).values()
    print(all_offers)

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
        for offer in all_offers:
            offer['fav'] = myuser.fav_offers.filter(id=offer['id']).exists()
    return render(request, 'offer/search.html', {'title':'پیشیاب', 'myuser':myuser, 'myoffers': all_offers})


def set_priority(request, offer_id):
    username = request.session.get("username")
    offer = Offer.objects.get(id=offer_id)
    provider = offer.user
    if username != provider.username:
        return redirect('index')

    if request.method == 'POST':
        priority = request.POST['prio_select']
        offer.priority = priority
        offer.save()
        messages.success(request, f'پیشنهاد شما اضافه شد!')
        return redirect('/profile/'+username)

    return render(request, 'offer/set_priority.html', {'title':'سطح پیشنهاد'})