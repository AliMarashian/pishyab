from os import truncate
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
    
class EditFormUser(forms.Form):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره موبایل")
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    password1 = forms.CharField(max_length = 20, label="رمز عبور جدید", widget=forms.PasswordInput())
    # password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور جدید", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

        
class EditFormProvider(forms.Form):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره تلفن")
    username = forms.CharField(max_length = 20, label="نام‌کاربری", required=False)
    password1 = forms.CharField(max_length = 20, label="رمز عبور جدید", widget=forms.PasswordInput(), required=False)
    # password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور جدید", widget=forms.PasswordInput())
    orgname = forms.CharField(max_length = 50, label="نام سازمان")
    address = forms.CharField(max_length = 100, label="آدرس سازمان", required=False)
    description = forms.CharField(max_length = 200, widget=forms.Textarea, label="توضیحات سازمان", required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    
    # title = forms.CharField(max_length = 50, label="عنوان")
    # description = forms.CharField(max_length = 200, widget=forms.Textarea, required=False, initial="", label="توضیحات")
    # start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="تاریخ شروع بازه پیشنهاد")
    # start_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), label="ساعت شروع بازه پیشنهاد")
    # end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="تاریخ پایان بازه پیشنهاد")
    # end_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), label="ساعت پایان بازه پیشنهاد")
    # price = forms.IntegerField(label="قیمت", required=False, validators=[MinValueValidator(0)], widget=forms.NumberInput(attrs={'placeholder': 'به ریال'}))
    # discount = forms.IntegerField(label="درصد تخفیف", required=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
   