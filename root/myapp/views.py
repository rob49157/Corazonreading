
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import AUTH
from django.contrib import messages
from .models import USER


def index(request):
    return render(request, 'index.html')

def register(request):

    if request.method == 'POST':

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if USER.objects.filter(email = email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif USER.objects.filter(username = username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            else:
                user= USER.objects.create_user(username= username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'not same password')
            return redirect('register')

    else:
        return render (request, 'register.html')
# Create your views here.
