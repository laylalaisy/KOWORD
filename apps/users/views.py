from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from . import forms
from . import models

class CustomBackend(ModelBackend):

	def authenticate(self, username=None, password=None, **kwargs):
		'''
		authenticate if user is valid to login
		'''
		try:
			user = UserProfile.objects.get(Q(username=username) | Q(email=username))
			if user.check_password(password): 	# password stored in backend is encrypted
				return user 					# success to login
		except Exception as e:
			return None							# fail to login

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
    	login_form = LoginFrom(request.POST)	# test if input is valid
    	if login_form.is_valid():				# input is valid, then get login inpu 
    		username_ = request.POST.get("username", "")
    		password_ = request.POST.get("password", "")
    		user = authenticate(username=username_, password=password_)	
    		if user is not None:				# user is valid
    			login(request, user)	
    			return render(reverse("index.html"))	# success to login
    		else:
    			return render(request, "login.html", {"msg": u"Username or password is wrong!"})	# fail to login
    	else:
            return render(request, "login.html", {"login_form": login_form})	# input is not valid

