from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Donation_list, UserUpdate

class UserSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields=['username','email','password']
		def save(self, commit=True):
			user = super().save(commit=False)
			user.is_User=True
			if commit:
				user.save()
			return user


class PoliceSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model =User
		fields=['username','email','password']
		def save(self,commit=True):
			user=super().save(commit=False)
			user.is_Police=True
			if commit:
				user.save()
			return user

class UserForm(forms.ModelForm):
	class Meta:
		model = UserUpdate
		fields =['f_name','l_name','city','phone','address']


class Dona_list(forms.ModelForm):
	class Meta:
		model = Donation_list
		fields = ['items']			