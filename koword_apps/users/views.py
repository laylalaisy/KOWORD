# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from .forms import LoginForm, RegisterForm
from .models import UserProfile


from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404


from django.shortcuts import redirect

from django.conf import settings

class CustomBackend(ModelBackend):
	def authenticate(self, username=None, password=None, **kwargs):
		try:
		  user = UserProfile.objects.get(Q(username=username)|Q(email=username))
		  if user.check_password(password): # password stored in backend is encrypted
		      return user 					# success to login
		except Exception as e:
			 return None							# fail to login


class LoginView(View):
    def get(self, request):
        return render(request, "user_login.html", {})

    def post(self, request):
    	loginform = LoginForm(request.POST)	# test if input is valid
    	if loginform.is_valid():				# input is valid, then get login inpu 
    		username = request.POST.get("username", "")
    		password = request.POST.get("password", "")
    		user = authenticate(username=username, password=password)	
    		if user is not None:				# user is valid
    			login(request, user)	
    			return render(request, "user_index.html", {
                    "msg": "success to login!"
                })	# success to login
    		else:
    			return render(request, "user_login.html", {  # fail to login
                    'loginform': loginform,
                    "msg": "Username or password is wrong!"
                })	
    	else:
            return render(request, "user_login.html", { # input is not valid
                'loginform': loginform
            }) 


class RegisterView(View):
    def get(self, request):
        registerform = RegisterForm()
        return render(request, "user_register.html", {
            'registerform':registerform,
        })

    def post(self, request):
        registerform = RegisterForm(request.POST)

        if registerform.is_valid():
            username = request.POST.get("username", "")
            if UserProfile.objects.filter(username=username):   # test if username is already exist
                return render(request, "user_register.html", {
                    "registerform":registerform,
                    "msg":"{0} is used. Please change another username!".format(username),
                })
            email = request.POST.get("email", "") 
            if UserProfile.objects.filter(email=email):   # test if email is already exist
                return render(request, "user_register.html", {
                    "registerform":registerform,
                    "msg":"{0} is used. Please change another email!".format(email),
                })
            password = request.POST.get("password", "")

            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.is_active = True
            user_profile.save()

            return render(request, "user_login.html", {
                "registerform": registerform,
                "msg": "Success to register! Please login now."
            })
        else:
            return render(request, "user_register.html", {
                "registerform": registerform,
                "msg": "Fail to register!"
            })

class IndexView(View):
    def get(self, request):
        #registerform = RegisterForm()
        return render(request, "user_index.html", {
            #'registerform':registerform,
        })