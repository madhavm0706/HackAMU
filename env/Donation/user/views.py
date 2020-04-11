from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserSignUpForm,PoliceSignUpForm,Dona_list, UserForm
from django.db.models import Q

from .models import User,Donation_list, UserUpdate


# Create your views here.

def index(request):
    return render(request,'donation/index.html')


def Logout(request):
	if request.user.is_user:
		logout(request)
		return redirect("ulogin")
	elif request.user.is_police:
		logout(request)
		return redirect("plogin")	

# Creating User Account
def userRegister(request):
	form =UserSignUpForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_user=True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return render(request,'donation/profile.html')
	context ={
		'form':form
	}			
	return render(request,'donation/user.html',context)


def UserLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_user:
				login(request,user)
				return redirect('ucreate')
			else:
				return render(request,'donation/userlogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'donation/userlogin.html',{'error_message': 'Invalid Login'})
	return render(request,'donation/userlogin.html')

#Create User profile 
def createUser(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("uprofile")
	context={
	'form':form,
	'title':"Complete Your profile"
	}
	return render(request,'donation/profile.html',context)	

#  Update customer detail
def updateUser(request,id):
	
	form  	 = UserForm(request.POST or None,instance=request.user)
	if form.is_valid():
		form.save()
		return redirect('uprofile')
	context={
	'form':form,
	'title':"Update Your profile"
	}
	return render(request,'donation/userprofile.html',context)	


# customer profile view
def UserProfile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
		user=request.user
	
	return render(request,'donation/profile.html',{'user':user})	

def dona_list(request):
	if request.method == 'POST':
		items = request.POST['items']
		quantity = request.POST['quantity']
		dona = Donation_list.objects.create(items=items,quantitiy=quantity)
		dona.save()
		return render(request,'donation/donation1.html')

	
	return render(request,'donation/donation.html')



# Showing Donar list to Police
def donar(request):
	r_object = UserUpdate.objects.all()
	query 	= request.GET.get('q')
	if query:
		r_object=UserUpdate.objects.filter(Q(rname__icontains=query)).distinct()
		return render(request,'donation/donar.html',{'r_object':r_object})
	return render(request,'donation/donar.html',{'r_object':r_object})


    


# creating Police account
def policeRegister(request):
	form =PoliceSignUpForm(request.POST or None)
	if form.is_valid():
		user      = form.save(commit=False)
		username  =	form.cleaned_data['username']
		password  = form.cleaned_data['password']
		user.is_police=True
		user.set_password(password)
		user.save()
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return render(request,'donation/index1.html')
	context ={
		'form':form
	}			
	return render(request,'donation/police.html',context) 


def PoliceLogin(request):
	if request.method=="POST":
		username = request.POST['username']
		password = request.POST['password']
		user     = authenticate(username=username,password=password)
		if user is not None:
			if user.is_police:
				login(request,user)
				return render(request,'donation/index1.html')
			else:
				return render(request,'donation/policelogin.html',{'error_message':'Your account disable'})
		else:
			return render(request,'donation/policelogin.html',{'error_message': 'Invalid Login'})
	return render(request,'donation/policelogin.html')	


