from django.shortcuts import render,redirect 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def registration_login(request):
    return render(request,"user/signup.html")

def add_user(request):
    name=request.POST["name"]
    email=request.POST["email"]
    password=request.POST["password"]
    user=User(username=name, email=email,password=password)
    
    user.save()

    messages.success(request , "account created")

    return HttpResponseRedirect(reverse('reglog'))


def user_login(request):
    name=request.POST["name"]
    password=request.POST["password"]
    user=authenticate(username=name,password=password)

    if user is not None:
        login(request,user)
        messages.success(request , "login successful")
        return HttpResponseRedirect(reverse('home'))
    else:
        print("wrong digits")
        messages.error(request , "incorrect credentials")
        return HttpResponseRedirect(reverse('reglog'))

    


def user_logout(request):
    logout(request)

    return redirect('home')




    
