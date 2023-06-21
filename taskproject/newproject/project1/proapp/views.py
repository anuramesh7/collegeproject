from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import redirect,render


def home(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"user invalid")
            return render(request,'login.html')
    return render(request,"login.html")

def form(request):
    return render(request,'form.html')

def thanks(request):
    return render(request,'thanks.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        CPassword = request.POST['password1']
        if password==CPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')


        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')


    return render(request,"register.html")