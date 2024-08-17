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
        print(username, password)
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
        print(Groups)
        if len(Groups)==0 and Groups[0].name !='customer':
            messages.error(request,'you are not authorised to login!')
            return redirect('login')
        login(request,user)
        return redirect('dashboard')
    return render(request, 'accounts/login_c.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if not username:
            messages.error(request,'username is a required field')
            return redirect('register')
        if not password:
            messages.error(request,'password is a required field')
            return redirect('register')
        if not cpassword:
            messages.error(request,'confirm password is a required field')
            return redirect('register')
        if not email:
            messages.error(request,'email is a required field')
            return redirect('register')
        if not first_name:
            messages.error(request,'first name is a required field')
            return redirect('register')
        if not last_name:
            messages.error(request,'last name is a required field')
            return redirect('register')
        if password!=cpassword:
            messages.error(request,'passwords do not match')
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'username is already taken')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'email is already taken')
            return redirect('register')
        user = User(username=username, email=email,first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        group = Group.objects.get(name='cutomer')
        user.groups.add(group)
        group.save()
        messages.success(request,'account created successfully')
        return redirect('login')
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
    logout(request)
    return redirect('index')

