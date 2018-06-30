# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from users.models import UserProfile
from books.models import List
from .models import Word, Record

class LearnBookListView(View):
    def get(self, request):
    	books = List.objects.all()

    	return render(request, "learn_list.html", {
    		"books": books
    	})


class LearnUnitListView(View):
	def get(self, request, book_id):
		books = List.objects.filter(id=book_id)
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname).values("unit").distinct()

		return render(request, 'learn_unit.html', {
			"books": books,
			"words": words
		})

class LearnWordListView(View):
	def get(self, request, book_id, word_unit):
		books = List.objects.filter(id=book_id)
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname, unit=word_unit)

		return render(request, 'learn_word.html', {
			"books": books,
			"unit": word_unit,
			"words": words
		})

class LearnFinishView(View):
	def get(self, request, book_id, word_unit, user_id):

		learn_record = Record()
		learn_record.isfinished = 1
		learn_record.userid = user_id
		learn_record.bookid = book_id
		learn_record.unit = word_unit
		learn_record.save()

		books = List.objects.all()

		return render(request, "learn_list.html", {
			"books": books
		})
