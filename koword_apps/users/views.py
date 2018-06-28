from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .forms import LoginForm
from .models import UserProfile

# -*- coding: utf-8 -*-
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.generic import View
#from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.conf import settings

class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		'''
		authenticate if user is valid to login
		'''
		try:
			user = UserProfile.objects.get(Q(username=username)|Q(email=username))
			if user.check_password(password): 	# password stored in backend is encrypted
				return user 					# success to login
		except Exception as e:
			return None							# fail to login

class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
    	login_form = LoginForm(request.POST)	# test if input is valid
    	if login_form.is_valid():				# input is valid, then get login inpu 
    		username_ = request.POST.get("username", "")
    		password_ = request.POST.get("password", "")
    		user = authenticate(username=username_, password=password_)	
    		if user is not None:				# user is valid
    			login(request, user)	
    			return render(reverse("index.html"))	# success to login}
    		else:
    			return render(request, "login.html", {"msg": u"Username or password is wrong!", "login_form": login_form})	# fail to login
    	else:
            return render(request, "login.html", {"msg": u"Username or password should be longer than 6 characters or numbers!", "login_form": login_form}) # input is not valid

