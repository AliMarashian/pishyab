from email.policy import default
from django import forms
from .models import Offer
from django.core.validators import MaxValueValidator, MinValueValidator
  

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'
  
class NewOfferForm(forms.Form):
    title = forms.CharField(max_length = 50, label="عنوان")
    description = forms.CharField(max_length = 200, widget=forms.Textarea, required=False, initial="", label="توضیحات")
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="تاریخ شروع بازه پیشنهاد")
    start_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), label="ساعت شروع بازه پیشنهاد")
    end_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), label="تاریخ پایان بازه پیشنهاد")
    end_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'type': 'time'}), label="ساعت پایان بازه پیشنهاد")
    price = forms.IntegerField(label="قیمت", required=False, validators=[MinValueValidator(0)], widget=forms.NumberInput(attrs={'placeholder': 'به ریال'}))
    discount = forms.IntegerField(label="درصد تخفیف", required=False, validators=[MaxValueValidator(100), MinValueValidator(0)])
    # email = forms.EmailField(label="ایمیل")
    # phone_no = forms.CharField(max_length = 20, label="شماره تلفن")
    # username = forms.CharField(max_length = 20, label="نام‌کاربری")
    # password1 = forms.CharField(max_length = 20, label="رمز عبور", widget=forms.PasswordInput())
    # password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور", widget=forms.PasswordInput())
    # orgname = forms.CharField(max_length = 20, label="نام سازمان")
    # class Meta:
    #     model = Offer
    #     fields = ['title', 'description', 'start_date', 'end_date', 'price', 'percentage']