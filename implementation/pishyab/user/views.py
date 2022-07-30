import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm, ProviderRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import MyUser
from offer.models import Offer
from django.contrib.auth.models import User

# from django.conf import settings
# User = settings.AUTH_USER_MODEL
   
   
#################### index ####################################### 
# def index(request):
#     # user = User(email="salam")
#     # user.save()
#     # print(user)
#     # print(User.objects.get(id="1").orgname)
#     return render(request, 'user/index.html', {'title':'پیشیاب'})
   
########### register here ##################################### 
def register(request):
    username = request.session.get("username")
    if username != None:
        return redirect('index')
    if request.method == 'POST':
        is_provider = ('orgname' in request.POST)
        if is_provider:
            form_provider = ProviderRegisterForm(request.POST)
            form = form_provider
        else:
            form_user = UserRegisterForm(request.POST)
            form = form_user
        if form.is_valid():
            form.save()
            cleaned_form = form.cleaned_data
            user = User.objects.get(username=cleaned_form.get("username"))
            my_user = MyUser(user=user, is_provider=is_provider, phone_no=cleaned_form.get("phone_no"), orgname=cleaned_form.get("orgname"))
            my_user.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system #################################### 
            htmly = get_template('user/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'pishyab@zohomail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ################################################################## 
            messages.success(request, f'حساب کاربری شما ساخته شد!')
            return redirect('login')
    else:
        form_user = UserRegisterForm()
        form_provider = ProviderRegisterForm()
    return render(request, 'user/register.html', {'form_user': form_user, 'form_provider': form_provider, 'title':'ثبت‌نام'})
   
################ login forms################################################### 
def Login(request):
    username = request.session.get("username")
    if username != None:
        return redirect('index')
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            # messages.success(request, f' خوش آمدید {username} !!!')
            request.session['username'] = user.username
            return redirect('index')
        else:
            messages.info(request, f'اطلاعات کاربری درست نمی‌باشد!')
    form = UserLoginForm()
    return render(request, 'user/login.html', {'form':form, 'title':'ورود'})


def view_profile(request, username_):
    user_of_interest = User.objects.get(username = username_)
    my_user_to_show = MyUser.objects.get(user = user_of_interest)
    
    my_offers = Offer.objects.all().values()
    user_offers = []

    for offer in my_offers:
        if User.objects.get(id = offer['user_id']).username == username_:
            user_offers.append(offer)

    context = {
        'user_toshow' : user_of_interest,
        'myuser_toshow': my_user_to_show,
        'myoffers' : user_offers,
    }

    print("*" * 100)
    return render(request, "user/profile.html", context)

def logout_view(request):
    logout(request)
    all_offers = Offer.objects.all().values()

    for offer in all_offers:
        initial_user = User.objects.get(id = offer['user_id'])
        my_user = MyUser.objects.get(user = initial_user)
        offer['orgname'] = my_user.orgname
        offer['username'] = initial_user.username

    # return render(request, "offer/view_offers.html", context)
    myuser = None
    return render(request, 'home/index.html', {'title':'پیشیاب', 'myuser':myuser, 'myoffers': all_offers})