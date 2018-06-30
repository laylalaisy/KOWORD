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
from learn.models import Word
from .models import Record

class ReviewBookListView(View):
    def get(self, request):
    	books = List.objects.all()

    	return render(request, "review_list.html", {
    		"books": books
    	})


class ReviewUnitListView(View):
	def get(self, request, book_id):
		books = List.objects.filter(id=book_id)
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname).values("unit").distinct()

		return render(request, 'review_unit.html', {
			"books": books,
			"words": words
		})

class ReviewWordListView(View):
	def get(self, request, book_id, word_unit):
		books = List.objects.filter(id=book_id)
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname, unit=word_unit)

		return render(request, 'review_word.html', {
			"books": books,
			"unit": word_unit,
			"words": words
		})

class ReviewFinishView(View):
	def get(self, request, book_id, word_unit, user_id):

		review_record = Record()
		review_record.isreviewed = 1
		review_record.userid = user_id
		review_record.bookid = book_id
		review_record.unit = word_unit
		review_record.save()

		books = List.objects.all()

		return render(request, "review_list.html", {
			"books": books
		})
