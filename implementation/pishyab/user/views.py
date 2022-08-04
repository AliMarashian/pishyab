from asyncio.windows_events import NULL
import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm, ProviderRegisterForm, EditFormProvider, EditFormUser
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import MyUser
from offer.models import Offer
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

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
    if username != None and User.objects.filter(username = username).exists():
        return redirect('index')
    form_provider = ProviderRegisterForm(request.POST or None)
    form_user = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        is_provider = ('orgname' in request.POST)
        if is_provider:
            form = form_provider
        else:
            form = form_user
        if form.is_valid():
            form.save()
            cleaned_form = form.cleaned_data
            user = User.objects.get(username=cleaned_form.get("username"))
            ################## TODO
            if is_provider:
                is_verified = True
            else:
                is_verified = True
            my_user = MyUser(user=user, is_provider=is_provider, phone_no=cleaned_form.get("phone_no"), orgname=cleaned_form.get("orgname"), address=cleaned_form.get('address'), description=cleaned_form.get('description'), license_link=cleaned_form.get('license_link'), is_verified=is_verified)
            if cleaned_form.get("pic_link"):
                my_user.pic_link = cleaned_form.get("pic_link")
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
            # msg.send()
            ################################################################## 
            messages.success(request, f'حساب کاربری شما ساخته شد!')
            return redirect('login')
        
    else:
        form_user = UserRegisterForm()
        form_provider = ProviderRegisterForm()
    return render(request, 'user/register.html', {'form_user': form_user, 'form_provider': form_provider, 'title':'ثبت‌نام'})
   
################ login forms################################################### 
def Login(request):
    print("man mikham biam too")
    username = request.session.get("username")
    if username != None and User.objects.filter(username = username).exists():
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
    
    user_offers = Offer.objects.filter(user=user_of_interest).values()
    fav_offers = my_user_to_show.fav_offers.all().values()
    fav_providers = my_user_to_show.fav_providers.all().values()
    for provider in fav_providers:
        provider["username"] = User.objects.get(id=provider["user_id"]).username

    username = request.session.get("username")
    myuser = None
    is_fav = False
    if username != None and User.objects.filter(username = username).exists():
        user = User.objects.get(username=username)
        myuser = MyUser.objects.get(user=user)
        for offer in user_offers:
            offer['fav'] = myuser.fav_offers.filter(id=offer['id']).exists()
        for offer in fav_offers:
            offer['fav'] = myuser.fav_offers.filter(id=offer['id']).exists()
        is_fav = myuser.fav_providers.filter(user=user_of_interest).exists()

    context = {
        'user_toshow' : user_of_interest,
        'myuser_toshow': my_user_to_show,
        'myoffers' : user_offers,
        'fav_offers' : fav_offers,
        'fav_providers' : fav_providers,
        'is_fav' : is_fav
    }

    # print("*" * 100)
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

def delete_view(request, username_):
    username = request.session.get("username")
    if username_ == username:   
        print(username + " is going to be deleted baby")
        user_ = User.objects.get(username = username_)
        myuser = MyUser.objects.get(user = user_)
        myuser.delete()
        user_.delete()
        return redirect('index')
    else:
        return redirect('index')

def edit_view(request, username_):
    username = request.session.get("username")
    if username_ == username:    
        if request.method == 'POST':
            is_provider = ('orgname' in request.POST)
            if is_provider:
                print('is provider')
                form_provider = EditFormProvider(request.POST)
                # form_provider.fields['username'].disabled = True
                form = form_provider
            else:
                print('is user')
                form_user = EditFormUser(request.POST)
                # form_user.fields['username'].disabled = True
                form = form_user
            if form.is_valid():
                print('form is valid')
                user_ = User.objects.get(username = username_)
                print(user_)
                myuser = MyUser.objects.get(user = user_)
                cleaned_form = form.cleaned_data
                if form.cleaned_data.get('email') != "":
                    user_.email = form.cleaned_data.get('email')
                print(form.cleaned_data.get('password1'))
                if form.cleaned_data.get('password1') != "":
                    user_.set_password(form.cleaned_data.get('password1'))
                user_.save()
                myuser.user = user_
                if cleaned_form.get("phone_no") != "":
                    myuser.phone_no = cleaned_form.get("phone_no")
                if is_provider and cleaned_form.get("orgname")!= "":
                    myuser.orgname = cleaned_form.get("orgname")
                if is_provider and cleaned_form.get("address")!= "":
                    myuser.address = cleaned_form.get("address")
                if is_provider and cleaned_form.get("description")!= "":
                    myuser.description = cleaned_form.get("description")   
                myuser.save()
                ################################################################## 
                messages.success(request, f'حساب کاربری شما بروزرسانی شد')
                return redirect('/profile/' + username)
            else:
                print(form.errors)
                print('form not valid')
                return redirect('/profile/' + username)
                # return redirect('index')
        else:
           print('whaaaaat')
           user_ = User.objects.get(username = username_)
           myuser = MyUser.objects.get(user = user_)
           print(myuser.is_provider)
           if myuser.is_provider:
                form = EditFormProvider(initial = {'username' : username_, 'email' : myuser.user.email, 'phone_no' : myuser.phone_no, 'orgname' : myuser.orgname, 'address': myuser.address, 'description': myuser.description})
                form.fields['description'].required = False
                form.fields['address'].required = False
           else:
                form = EditFormUser(initial = {'username' : username_, 'email' : myuser.user.email, 'phone_no' : myuser.phone_no})
           form.fields['username'].disabled = True
           form.fields['username'].required = False
           form.fields['password1'].required = False
        #    form.fields['password2'].required = False
           context = {'form':form, 'myuser': myuser, 'title':"ویرایش پروفایل"}
           return render(request,'user/edit.html',context)

    else:
        return redirect('index')

@ login_required
def fav_offer(request, offer_id):
    offer = Offer.objects.get(id=offer_id)   #TODO: try catch
    username = request.session.get("username")
    user = User.objects.get(username=username)
    myuser = MyUser.objects.get(user=user)
    if myuser.fav_offers.filter(id=offer_id).exists():
        myuser.fav_offers.remove(offer)
    else:
        myuser.fav_offers.add(offer)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@ login_required
def fav_provider(request, user_id):
    target_user = User.objects.get(id=user_id)   #TODO: try catch
    target_myuser = MyUser.objects.get(user=target_user)
    username = request.session.get("username")
    user = User.objects.get(username=username)
    myuser = MyUser.objects.get(user=user)
    print(myuser.fav_providers.all())
    if myuser.fav_providers.filter(user=target_user).exists():
        myuser.fav_providers.remove(target_myuser)
    else:
        myuser.fav_providers.add(target_myuser)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

