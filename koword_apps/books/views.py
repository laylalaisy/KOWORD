# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from .models import List

class BooksListView(View):
    def get(self, request):
    	books = List.objects.all()

    	return render(request, "books_list.html", {
    		"books": books
    	})