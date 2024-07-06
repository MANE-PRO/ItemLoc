from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
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
            return redirect('signup')
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
    return render(request, 'signin/signup.html')
def logout(request):
    auth.logout(request)
    return redirect('signin')