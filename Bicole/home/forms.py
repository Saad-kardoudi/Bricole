from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreationUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
		widgets = {
			'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'inputs'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'inputs'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'inputs'}),
			'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'inputs'}),
			'password1': forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Password'}),
			'password2': forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': 'Confirm Your Password'}),
		}


class EditionUserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']
		widgets = {
			'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'inputs'}),
			'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'inputs'}),
		}


class CreationAccountForm(ModelForm):
	class Meta:
		model = Account
		fields = ['user', 'phone', 'city', 'country', 'adress']
		widgets = {
			'user': forms.TextInput(attrs={'style': 'visibility: hidden;'}),
			'phone': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'inputs'}),
			'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'inputs'}),
			'country': forms.TextInput(attrs={'placeholder': 'Country', 'class': 'inputs'}),
			'adress': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'inputs'}),
		}


class EditAccountForm(ModelForm):
	class Meta:
		Available_choices = (
			('Not Available', 'Not Available'),
			('Available', 'Available'),
			('Available form now', 'Available form now'))
		model = Account
		fields = ['job', 'bio', 'city', 'Available', 'Acc_pic']
		widgets = {
			'job': forms.TextInput(attrs={'placeholder': 'job', 'class': 'inputs'}),
			'bio': forms.Textarea(attrs={"rows": 6, "cols": 30, 'class': 'textarea-inputs', 'placeholder': 'Bio.. Write something about stuff you can do ...'}),
			'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'textarea-inputs'}),
			'Available': forms.Select(choices=Available_choices, attrs={'placeholder': 'Available', 'class': 'textarea-inputs'}),
			'Acc_pic': forms.FileInput(attrs={'id': "upload-photo", 'class': 'upload-photo', 'onchange': 'previewFile(this)'})
		}


class CreationRatingForm(ModelForm):
	class Meta:
		model = Rating
		fields = ['Worker', 'employer', 'Comment', 'rate']
		widgets = {
			'Worker': forms.TextInput(attrs={'style': 'visibility: hidden;'}),
			'employer': forms.TextInput(attrs={'style': 'visibility: hidden;'}),
			'Comment': forms.Textarea(attrs={"rows": 2, "cols": 30, 'class': 'textarea-inputs', 'placeholder': 'Comment'}),
			'rate': forms.NumberInput(attrs={'class': 'rating'}),
		}


class CreationHireMeForm(ModelForm):
	class Meta:
		model = Hire_me
		fields = ['Worker', 'employer', 'Disciption']
		widgets = {
			'Worker': forms.TextInput(attrs={'style': 'visibility: hidden;'}),
			'employer': forms.TextInput(attrs={'style': 'visibility: hidden;'}),
			'Disciption': forms.Textarea(attrs={"rows": 2, "cols": 30, 'class': 'textarea-inputs', 'placeholder': 'describe your mini job '}),
		}