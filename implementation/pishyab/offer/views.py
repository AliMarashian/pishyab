from django.shortcuts import render, redirect
from .forms import NewOfferForm
from django.contrib import messages
from .models import Offer
from django.contrib.auth.models import User



def new_offer(request):

    # Check if user is logged in as provider

    if request.method == 'POST':
        form = NewOfferForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            try:
                username = request.session.get("username")
                user = User.objects.get(pk=1)
                print(username, user, user.email)
            except:
                print("ERROR | New_Offer | No User")
                return render(request, 'offer/new_offer.html', {'form': form, 'title':'پیشنهاد جدید'})

            print(user)
            new_offer = Offer(user=user, title=cleaned_form.get("title"), description=cleaned_form.get("description"), start_date=cleaned_form.get("start_date"), start_time=cleaned_form.get("start_time"),
                end_date=cleaned_form.get("end_date"), end_time=cleaned_form.get("end_time"), price=cleaned_form.get("price"), discount=cleaned_form.get("discount"))
            new_offer.save()

            ################################################################## 
            messages.success(request, f'پیشنهاد شما اضافه شد!')
            return redirect('view_offers')
    else:
        form = NewOfferForm()
    return render(request, 'offer/new_offer.html', {'form': form, 'title':'پیشنهاد جدید'})
   


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