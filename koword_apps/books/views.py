# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.views.generic import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404


from django.shortcuts import redirect

from django.conf import settings

class BooksListView(View):
    def get(self, request):
        return render(request, "books_list.html", {})