# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Answer(models.Model):
    text = models.CharField(max_length=100)
    category = models.CharField(max_length=12)

class Question(models.Model):
    text = models.CharField(max_length=250)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=12)

class Quiz(models.Model):
    name = models.CharField(max_length=20)

class QuizContents(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
class Record(models.Model):
    officer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_given = models.ForeignKey(Answer, on_delete=models.CASCADE)
    
