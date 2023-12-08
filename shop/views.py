from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

def home(request):
    all_products = Product.objects.all()
    return render(request, 'index.html', context={'products': all_products})


def about(request):
    return render(request, 'about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('home')
        else:
            messages.success(request, 'مشکلی در ورود شما وجود دارد')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "با موفقیت خارج شدید!")
    return redirect("home")


def product(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "product.html", {"product": product})

def cart(request):
    return render(request, "cartbox.html")

def signup_user(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            messages.success(request,'اکانت شما با موفقیت ساخته شد')
        else:
            messages.success(request, 'اکانت شما با مشکلی مواجه شد')
            return redirect('signup')
    else:
        return render(request, 'signup.html', context={'form':form})
