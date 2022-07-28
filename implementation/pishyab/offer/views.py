from django.shortcuts import render, redirect
from forms import NewOfferForm
from django.contrib import messages



def new_offer(request):

    # Check if user is logged in as provider

    if request.method == 'POST':
        form = NewOfferForm(request.POST)
        if form.is_valid():
            
            ################################################################## 
            messages.success(request, f'پیشنهاد شما اضافه شد!')
            return redirect('home/index')
    else:
        form = NewOfferForm()
    return render(request, 'offer/new_offer.html', {'form': form, 'title':'پیشنهاد جدید'})
   