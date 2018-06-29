# -*- coding: utf-8 -*-
import json

from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=6, max_length=20)
	password = forms.CharField(required=True, min_length=6, max_length=100)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=6, max_length=20)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=100)
    password_confirm = forms.CharField(required=True, min_length=6, max_length=100)

    def is_valid(self): # passwords should be same
        if self.is_bound:
            if self.data['password'] != self.data['password_confirm']:
                self.add_error("password_confirm", "Passwords are not same!")
        return super(RegisterForm, self).is_valid()

