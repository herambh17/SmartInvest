from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout



def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        if User.objects.filter(username=username).exists():
            return HttpResponse('Username already taken, please choose another.', status=400)
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
            return HttpResponse('Email already taken, please choose another.', status=400)
        password=request.POST['password']
        user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        user.save()
        
        return redirect('/signin')
    else:
        return render(request, 'signup.html')


def home(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('http://localhost:8501')
    else:
        return redirect('/signin')

def signout(request):
    logout(request)
    return redirect('/signin')
    

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
          
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
          
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/signin')
             

        else:
            return render(request,'login.html')

# Create your views here.
