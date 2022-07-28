from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import MyUser
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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            cleaned_form = form.cleaned_data
            user = User.objects.get(username=cleaned_form.get("username"))
            my_user = MyUser(user=user, phone_no=cleaned_form.get("phone_no"), orgname=cleaned_form.get("orgname"))
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
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title':'ثبت‌نام'})
   
################ login forms################################################### 
def Login(request):
    if request.method == 'POST':
   
        # AuthenticationForm_can_also_be_used__
   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' خوش آمدید {username} !!!')
            request.session['username'] = user.username
            return redirect('index')
        else:
            messages.info(request, f'اطلاعات کاربری درست نمی‌باشد!')
    form = UserLoginForm()
    return render(request, 'user/login.html', {'form':form, 'title':'ورود'})