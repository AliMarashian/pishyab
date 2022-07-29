from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
  
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    password = forms.CharField(max_length = 20, label="رمز عبور", widget=forms.PasswordInput())
    # last_name = forms.CharField(max_length = 20)
    # class Meta:
    #     model = User
    #     fields = ['username', 'password1']

  
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره تلفن")
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    password1 = forms.CharField(max_length = 20, label="رمز عبور", widget=forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class ProviderRegisterForm(UserCreationForm):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره تلفن")
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    password1 = forms.CharField(max_length = 20, label="رمز عبور", widget=forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور", widget=forms.PasswordInput())
    orgname = forms.CharField(max_length = 50, label="نام سازمان")
    address = forms.CharField(max_length = 100, label="آدرس سازمان")
    description = forms.CharField(max_length = 200, widget=forms.Textarea, label="توضیحات سازمان")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']