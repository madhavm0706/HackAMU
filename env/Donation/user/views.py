from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'user/index.html',{})


def UserLogin(request):
    return render(request,'user/dlogin.html',{})

def PoliceLogin(request):
    return render(request,'user/plogin.html',{})    
