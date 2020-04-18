from django.shortcuts import render,redirect
from useraccount import models
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login,authenticate

# Create your views here.

def signup(request):

    if request.method   == 'POST':

        givenname       =   request.POST.get("givenname")
        surename        =   request.POST.get("surename")
        email           =   request.POST.get("email")
        username        =   request.POST.get("username")
        password1       =   request.POST.get("password1")
        password2       =   request.POST.get("password2")

        if password1 == password2 :
            
            if User.objects.filter(username=username).exists():

                messages.info(request,'username already exists')
                return redirect('signup')
            
            elif User.objects.filter(email=email).exists():

                messages.info(request,'email already used ')
                return redirect('signup')

            else:
                  
                user     =  User.objects.create_user(username=username,email=email,password=password1)
                user.save()

                sign     =  models.signup()
                sign.givenname  = givenname 
                sign.surename   = surename
                sign.username   = user
                sign.save()

                messages.info(request,'User Creation Successful')
                return redirect('signup')




        else:
            
            messages.info(request,'Password Must Match..')
            return redirect('signup')


    else:
        
        return render(request,'account/signup.html')


def login(request):
 
    if request.method   ==  'POST':

        username        =   request.POST.get("username")
        password        =   request.POST.get("password")

        user = auth.authenticate(username=username,password=password)

        if user is not None:

            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request,'user name or password is not matching...')
            return redirect('login')

    else:
        
        return render(request,'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')