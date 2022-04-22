from django.shortcuts import render,redirect
from .forms import *
from .models import AdminTable
from django.contrib import messages
# Create your views here.

def register_admin(req):
    if req.method=='POST':
        form = AdminForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Admin Register Successfully...")
            return redirect("Login")
        else:
            messages.error(req,"Registration Unsuccessfull, Something went wrong...")
    else:
        form = AdminForm()
    context = {'form':form}
    return render(req,'accounts/registration.html',context)


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
def mylogin(req):
    print(req.method)
    if req.method=='POST':
        form = AuthenticationForm(req.POST)
        email = req.POST['username']
        password = req.POST['password']
        if email and password:
            user = authenticate(req,username=email,password=password)
            if user:
                login(req,user)
                messages.success(req,"Login Successfull.")
                return redirect("Home")
            else:
                messages.error(req,"Invalid username or Password")
        else:
            messages.error(req,"please Enter the username and Password")
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(req,'accounts/login.html',context)


def mylogout(req):
    logout(req)
    messages.warning(req,"Logout Successfull...")
    return redirect("Home")