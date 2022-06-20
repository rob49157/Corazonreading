
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
# from .models import USER


def index(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':

        username = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']
        password2 = request.POST.get['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'not same password')
            return redirect('register')

    else:
        return render(request, 'register.html')
# Create your views here.
