from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
# Create your views here.

def index(request):  
    
    if request.user.is_anonymous:
        print(request)
        
        return redirect("/login")
    return render(request,'index.html')
def loginUser(request):
    
    if request.method=="POST":
        username= request.POST.get("username")
        password= request.POST.get("password")
        # check if user has entered correctly 
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request, 'Wrong username or password')
            return render(request,'login.html')
    return render(request,'login.html')
def logoutUser(request):
    logout(request) 
    # inbuilt function to logout
    return redirect(request,'login.html')