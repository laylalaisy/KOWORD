# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from books.models import List
from .models import Word

class LearnBookListView(View):
    def get(self, request):
    	books = List.objects.all()

    	return render(request, "learn_list.html", {
    		"books": books
    	})


class LearnUnitListView(View):
	def get(self, request, book_id):
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname)

		return render(request, 'learn_unit.html', {
			"words": words
		})
