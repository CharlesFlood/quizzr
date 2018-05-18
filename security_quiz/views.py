# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from random import sample, shuffle

from .models import Record, Quiz, Question ,Answer

# Create your views here.
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
    ### Quiz list will currently just depend on your permissions
    ### This will be split depending on how recently the quiz was taken
    
    
    quiz_list = Quiz.objects.all()
    #time_threshold = datetime.now() - timedelta(days=30)
    #pertinent_records = Record.objects.filter(officer=request.user)
    #latest_timestamps = {}
    #for r in pertinent_records:
    #    if not latest_timestamps[r.quiz] or r.timestamp > latest_timestamps[r.quiz]:
    #        latest_timestamps[r.quiz] = r.timestamp
    #qualified_list = Quiz.objects.filter

    context = {'quiz_list': quiz_list}
    return render(request, 'security_quiz/quiz_list.html', context)

@login_required
def quiz_results(request, quiz_num):
    return HttpResponse("Quiz results")

@login_required
def take_quiz(request, quiz_num):
    quiz = get_object_or_404(Quiz, pk=quiz_num)
    questions = Question.objects.filter(quizzes__id=quiz_num)
    question_ids=(q.id for q in questions)
    answers = Answer.objects.in_bulk(question_ids)
    number_of_answers = len(answers)

    question_set = []
    for q in questions:
        right_answer = Answer.objects.filter(pk=q.answer)
        answer_list = sample(answers, 5)
        if (right_answer not in answer_list):
            del answer_list[-1]
            answer_list.append(right_answer)
        shuffle(answer_list)
        question_set.append({'question': q, 'right_answer': right_answer, 'answer_list':answer_list})
    
    context = {'quiz': quiz, 'questions': question_set}
    
    return HttpResponse("This is the page where you actually take the quiz")

@login_required
def grade_quiz(request):
    ### should be POST 
    x=0

def random_unique_list(size):
    
