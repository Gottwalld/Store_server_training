from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'Users/login.html')

def registration(request):
    return render(request, 'Users/registration.html')