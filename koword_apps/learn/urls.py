"""koword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import LearnBookListView, LearnUnitListView, LearnWordListView, LearnFinishView, LearnRecordView

urlpatterns = [
    url(r'^booklist/$', LearnBookListView.as_view(), name='learn_booklist'),
    url(r'^unitlist/(?P<book_id>\d+)$', LearnUnitListView.as_view(), name='learn_unitlist'),
    url(r'^wordlist/(?P<book_id>\d+)/(?P<word_unit>\d+)$', LearnWordListView.as_view(), name='learn_wordlist'),
    url(r'^learned/(?P<book_id>\d+)/(?P<word_unit>\d+)/(?P<user_id>\d+)$', LearnFinishView.as_view(), name='learn_learned'),
    url(r'^record/$', LearnRecordView.as_view(), name='learn_record'),
]
