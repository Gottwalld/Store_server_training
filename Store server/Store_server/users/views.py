from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': UserLoginForm()}
    return render(request, 'Users/login.html', context)

def registration(request):
    return render(request, 'Users/registration.html')