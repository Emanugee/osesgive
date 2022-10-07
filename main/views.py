import requests
import uuid
import json

from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .forms import CartForm, RegisterForm
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    profile = User.objects.get(username = request.user.username)
    option = PaymentOption.objects.all()
    form = CartForm()
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = profile
            new.save()
            return redirect('confirm')
        else:
            messages.error(request, form.errors)
            return redirect('home')
        
    context = {
        'option':option, 
        'form':form, 
    }

    return render(request, 'home.html', context)

def confirm(request):
    info = Cart.objects.filter(user__username = request.user.username, paid= False).last()

    context = {
        'info':info
    }

    return render(request, 'confirm.html', context)


def signout(request):
    logout(request)
    messages.success(request, 'You are now Signed Out')
    return redirect('index')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'login successful!')
            return redirect('home')
        else:
            messages.info(request, 'Username/Password is incorrect, please try again.')
            return redirect('signin')

    return render(request, 'login.html')

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            newuser = Profile(user=user)
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email 
            newuser.phone = phone 
            newuser.save()
            messages.success(request, 'Your registration is successful')
            return redirect('signin')
        else:
            messages.error(request, form.errors)
            return redirect('signup')

    return render(request, 'register.html')

def payment(request):
    if request.method == 'POST':
        api_key = 'sk_test_ad502719e58fd78a40fd31ab9415532181331240'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://54.144.119.13/thanks' 
        ref = str(uuid.uuid4()) 
        profile = Profile.objects.get(user__username = request.user.username)
        amount = float(request.POST['amount']) * 100  
        user = User.objects.get(username = request.user.username)
        email = user.email 
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        purpose = request.POST['purpose']
 
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': ref, 'amount': int(amount), 'email': user.email, 'callback_url': cburl}
        
        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Network busy, try again')
        else:
            transback = json.loads(r.text)
            # print('TESTING DATA', transback)
            rdurl = transback['data']['authorization_url']

            account = Payment()
            account.user = user
            account.first_name = user.first_name
            account.last_name = user.last_name
            account.amount = amount/100
            account.email = user.email 
            account.paid = True 
            account.phone = phone
            account.purpose = purpose
            account.pay_code = ref 
            account.save()
            return redirect(rdurl)

    return redirect('confirm')

def thankyou(request):
    transact = Payment.objects.filter(user__username = request.user.username,paid= True).last()

    context = {
        'transact':transact 
    }
    
    return render(request, 'thank.html', context)