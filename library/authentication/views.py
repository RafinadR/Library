from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import CustomUser
from .decorators import librarian_required
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import messages
from django.core.exceptions import ValidationError



# Create your views here.


@login_required
def index_view(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse("authentication:login"))
    if CustomUser.get_role_name(request.user) == 'librarian':
        return render(request, "authentication/index_librarian.html", {
        "role" : CustomUser.get_role_name(request.user), 
    })
    return render(request, "authentication/index.html", {
        "role" : CustomUser.get_role_name(request.user), 
    })



def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,"Incorrect email or password" )
                return render(request, "authentication/login.html", {
                'form': form
            } )                  
    else:
        form = UserLoginForm()           
    return render(request, "authentication/login.html",{
        'form': form,
    })


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                messages.success(request, 'Registration was successful!')
                return redirect("authentication:login")     
            
    else:
        form = UserRegistrationForm()     
    return render(request, "authentication/registration.html", {
        'form': form
    })
   
    

        
