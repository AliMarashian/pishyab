from os import truncate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from location_field.forms.plain import PlainLocationField
  

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
    pic_link = forms.CharField(max_length = 400, label="لینک عکس پروفایل آپلود شده", required=False)
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    password1 = forms.CharField(max_length = 20, label="رمز عبور", widget=forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور", widget=forms.PasswordInput())
    #location = PlainLocationField(zoom=7, label='مختصات', based_fields=[], initial='35.699295968881565,51.3368797302246')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class ProviderRegisterForm(UserCreationForm):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره تلفن")
    pic_link = forms.CharField(max_length = 400, label="لینک عکس پروفایل آپلود شده", required=False)
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    password1 = forms.CharField(max_length = 20, label="رمز عبور", widget=forms.PasswordInput())
    password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور", widget=forms.PasswordInput())
    orgname = forms.CharField(max_length = 50, label="نام سازمان")
    address = forms.CharField(max_length = 100, label="آدرس سازمان")
    description = forms.CharField(max_length = 200, widget=forms.Textarea, label="توضیحات سازمان")
    license_link = forms.CharField(max_length = 400, label="لینک مجوز کسب آپلود شده")
    location = PlainLocationField(zoom=7, label='مختصات', based_fields=[], initial='35.699295968881565,51.3368797302246')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class EditFormUser(forms.Form):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره موبایل")
    username = forms.CharField(max_length = 20, label="نام‌کاربری")
    location = PlainLocationField(zoom=7, label='مختصات', based_fields=[], initial='35.699295968881565,51.3368797302246')
    # password1 = forms.CharField(max_length = 20, label="رمز عبور جدید", widget= forms.PasswordInput
    #                        (attrs={'id':'password_edit'}), required=False)
    # password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور جدید", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

        
class EditFormProvider(forms.Form):
    email = forms.EmailField(label="ایمیل")
    phone_no = forms.CharField(max_length = 20, label="شماره تلفن")
    username = forms.CharField(max_length = 20, label="نام‌کاربری", required=False)
    # password1 = forms.CharField(max_length = 20, label="رمز عبور جدید",widget= forms.PasswordInput
    #                        (attrs={'id':'password_edit', 'onchange': 'promptFunction()'}) , required=False)
    # password2 = forms.CharField(max_length = 20, label="تکرار رمز عبور جدید", widget=forms.PasswordInput())
    orgname = forms.CharField(max_length = 50, label="نام سازمان")
    address = forms.CharField(max_length = 100, label="آدرس سازمان", required=False)
    description = forms.CharField(max_length = 200, widget=forms.Textarea, label="توضیحات سازمان", required=False)
    location = PlainLocationField(zoom=7, label='مختصات', based_fields=[], initial='35.699295968881565,51.3368797302246')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    

class UserPasswordResetForm(SetPasswordForm):
    """Change password form."""
    new_password1 = forms.CharField(label='Password',
        help_text="<ul class='errorlist text-muted'><li>Your password can 't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can 't be a commonly used password.</li> <li>Your password can 't be entirely numeric.<li></ul>",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'password',
            'type': 'password',
            'id': 'user_password',
        }))

    new_password2 = forms.CharField(label='Confirm password',
        help_text=False,
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'confirm password',
            'type': 'password',
            'id': 'user_password',
        }))


class UserForgotPasswordForm(PasswordResetForm):
    """User forgot password, check via email form."""
    email = forms.EmailField(label='آدرس ایمیل',
        required=True,
        widget=forms.TextInput(
         attrs={'placeholder': 'برای مثال aaa@gmail.com',
                'type': 'text',
                'id': 'email_address'
                }
        ))