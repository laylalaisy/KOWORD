# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, "home.html", {})