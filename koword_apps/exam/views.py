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

class ExamBookListView(View):
    def get(self, request):
    	books = List.objects.all()

    	return render(request, "exam_list.html", {
    		"books": books
    	})


class ExamUnitListView(View):
	def get(self, request, book_id):
		books = List.objects.filter(id=book_id)
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname).values("unit").distinct()

		return render(request, 'exam_unit.html', {
			"books": books,
			"words": words
		})

class ExamWordListView(View):
	def get(self, request, book_id, word_unit):
		books = List.objects.filter(id=book_id)
		bookname = List.objects.filter(id=book_id).values("name")
		words = Word.objects.filter(bookname=bookname, unit=word_unit)

		return render(request, 'exam_word.html', {
			"books": books,
			"unit": word_unit,
			"words": words
		})

class ExamFinishView(View):
	def get(self, request, book_id, word_unit, user_id):

		exam_record = Record()
		exam_record.isexamed = 1
		exam_record.userid = user_id
		exam_record.bookid = book_id
		exam_record.unit = word_unit
		exam_record.save()

		books = List.objects.all()

		return render(request, "exam_list.html", {
			"books": books
		})

class ExamRecordView(View):
    def get(self, request):
    	books = List.objects.all()
    	records = Record.objects.filter(userid=request.user.id)

    	results = []
    	for book in books:
    		examed_count = Record.objects.filter(userid=request.user.id, bookid=book.id, isexamed=1).count()
    		results.append({
    			"bookname": book.name,
    			"unit": book.unit,
    			"examed_count": examwed_count,
    			"notexamed_count": book.unit - examed_count
    			})

    	return render(request, "exam_records.html", {
    		"books": books,
    		"records": results
    	})