# -*- coding: utf-8 -*-
import json

from django import forms

from .models import UserProfile

class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=6)
	password = forms.CharField(required=True, min_length=6)