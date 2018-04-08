# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Security Quiz index")

def user_profile(request):
    return HttpResponse("Insert User Profile here")

def quiz_list(request):
    return HttpResponse("This is a list of quizes")

def quiz_results(request, quiz_num):
    return HttpResponse("Quiz results")

def quiz(request, quiz_num):
    return HttpResponse("This is the page where you actually take the quiz")
