from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication import forms

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):

    if request.method=="POST":
        username= request.POST['username']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        email= request.POST['email']

        myuser=User.objects.create_user(username,pass1,email)
        myuser.save()

        messages.success(request," Your account has been successfully created")

        return redirect ('signin')


    return render(request,"authentication/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1= request.POST['pass1']

        user=authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html")

        else:
            messages.error(request, "Wrong Credentials")
            return redirect('home')


    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')



def email_signup(request):
    user = User.objects.all()
    if request.method=="POST":
        email = request.POST['email']
        for u in user:
            if email == u.email:
                return redirect(signin)
        else:
            return redirect(signup)
        
    return render(request, 'authentication/phone.html')
        