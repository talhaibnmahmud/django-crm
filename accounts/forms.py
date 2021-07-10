from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class CustomerForm(ModelForm):
	"""docstring for CustomerForm"""
	class Meta:
		"""docstring for Meta"""
		model = Customer
		fields = '__all__'
		exclude = ['user']
		


class OrderForm(ModelForm):
	"""docstring for OrderForm"""
	class Meta:
		"""docstring for Meta"""
		model = Order
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	"""docstring for ClassName"""
	class Meta:
		"""docstring for Meta"""
		model = User
		fields = ['username', 'email', 'password1', 'password2']
			
		
