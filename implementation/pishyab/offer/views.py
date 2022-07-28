from django.shortcuts import render, redirect
from .forms import NewOfferForm
from django.contrib import messages
from .models import Offer



def new_offer(request):

    # Check if user is logged in as provider

    if request.method == 'POST':
        form = NewOfferForm(request.POST)
        if form.is_valid():
            
            ################################################################## 
            messages.success(request, f'پیشنهاد شما اضافه شد!')
            return redirect('offer/view_offers')
    else:
        form = NewOfferForm()
    return render(request, 'offer/new_offer.html', {'form': form, 'title':'پیشنهاد جدید'})
   


def view_offers(request):

    my_offers = Offer.objects.all().values()
    # template = loader.get_template('view_schedule.html')
    context = {
        'myoffers': my_offers
    }
    
    return render(request, "offer/view_offers.html", context)