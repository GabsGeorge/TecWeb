from django.shortcuts import render

# Create your views here.

def login_admin(request):
    return render(request, "paineldecontrole/login.html")   

def registrar_admin(request):
    return render(request, "paineldecontrole/registrar.html")       
