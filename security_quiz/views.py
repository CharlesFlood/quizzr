# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

from .models import Record


class QuizList(ListView):
    model = Quiz


def index(request):
    return HttpResponse("Security Quiz index")

@login_required
def user_profile(request):
    ### User profile will show the user's name, have a link for
    ### reseting password, and a record of training completed
    completed_quizzes = Record.objects.filter(officer=request.user)
    context = {'completed_quizzes': completed_quizzes}
    return render(request, 'security_quiz/user_profile.html', context)


@login_required
def quiz_list(request):
    return HttpResponse("This is a list of quizes you have available")

@login_required
def quiz_results(request, quiz_num):
    return HttpResponse("Quiz results")

@login_required
def quiz(request, quiz_num):
    return HttpResponse("This is the page where you actually take the quiz")
