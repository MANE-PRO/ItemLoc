from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if(user is not None):
            auth.login(request, user)
            return redirect('index')
        else:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.ERROR, "Wrong Password", fail_silently=True)
            else:
                messages.add_message(request, messages.ERROR, "Username Not found. Please Sign Up!", fail_silently=True)
    return render(request, 'signin/signin.html')
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        if not(User.objects.filter(username = username).exists() or User.objects.filter(email = email).exists()):
            user = User.objects.create_user(username=username, email = email, password= password)
            auth.login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Username Already Exists!", fail_silently=True)
            return redirect('signin')
    return render(request, 'signin/signup.html')
def logout(request):
    auth.logout(request)
    return redirect('signin')