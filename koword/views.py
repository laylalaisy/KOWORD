from django.shortcuts import render
from django.views.generic import View

from . import forms

class LoginView(View)
	def get(self, request):
    	return render(request, "login.html", {})

    def post(self, request):
    	loginform = LoginFrom(request.POST)
