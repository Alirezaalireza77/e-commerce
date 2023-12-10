from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خود را وارد کنید:'})
    )
    last_name = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام خانوادگی خود را وارد کنید:'})
    )
    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل خود را وارد کنید:'})
    )
    username = forms.CharField(
        label="",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید:'})
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs=
               {'class': 'form-control',
                'name' : 'password',
                'type' : 'password',
                'placeholder': 'رمز بالای 8 کاراکتر خود را وارد کنید:'})
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs=
            {'class': 'form-control',
             'name': 'password',
             'type': 'password',
             'placeholder': 'دوباره رمز خود را وارد کنید:'})
    )

    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email', 'username', 'password1', 'password2')