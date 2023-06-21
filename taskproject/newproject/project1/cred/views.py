from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import redirect,render


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        # return redirect('/')

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"user invalid")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        CPassword = request.POST['password1']
        if password==CPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')


        else:
            messages.info(request, "Password Mismatch")
            return redirect('register')


    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('login')
from django.shortcuts import render

# Create your views here.
