from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def Userregister(request):
    form=RegisterForm()
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def Userlogin(request):
    if request.method == 'POST':
        u= request.POST.get('uname')
        p= request.POST.get('password')

        user=authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'Invalid cridential')
    template_name='login.html'
    return render(request,template_name)

def Userlogout(request):
    logout(request)
    return redirect('register')

def change_password(request):
    form=PasswordChangeForm(request.user)
    if request.method == 'POST':
        form =PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        
    
    template_name='change_password.html'
    context={'form':form}
    return render(request,template_name,context)

def homeview(request):
    template_name='home.html'
    context={}
    return render(request,template_name,context)



