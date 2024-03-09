from django.shortcuts import render
from users.forms import UserLoginForm

# Create your views here.
def login(request):
    context = {'form': UserLoginForm()}
    return render(request, 'Users/login.html', context)

def registration(request):
    return render(request, 'Users/registration.html')