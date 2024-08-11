from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group, User
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username:
            messages.error(request,'username is required')
            return redirect('login')
        if not password:
            messages.error(request,'password is required')
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if  user is None:
            messages.error(request,'invalid credentials')
            return redirect('login')
        if  not user.groups.exists():
            messages.error(request,'contact your administrator')
            return redirect('login')
        Groups= user.groups.all()
        if
    return render(request, 'accounts/login_c.html')

def register_view(request):
    return render(request, 'accounts/register_c.html')
def dashboard_view(request):
    return render(request, 'accounts/dashboard_c.html')
def slogin_view(request):
    return render(request, 'accounts/login_s.html')
def sregister_view(request):
    return render(request, 'accounts/register_s.html')
def sdashboard_view(request):
    return render(request, 'accounts/dashboard_s.html')
def logout_view(request):
    return redirect('index')

