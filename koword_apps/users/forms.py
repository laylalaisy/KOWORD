# -*- coding: utf-8 -*-
import json

from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=6, max_length=20)
	password = forms.CharField(required=True, min_length=6, max_length=200)


class RegisterForm(forms.Form):
    nickname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    password_confirm = forms.CharField(required=True, min_length=5)

    def is_valid(self):
        if self.is_bound:
            if self.data['password'] != self.data['password_confirm']:
                self.add_error("password_confirm", u"密码不一致")
        return super(RegisterForm, self).is_valid()

