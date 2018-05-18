# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Quiz(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "quizzes"

class Answer(models.Model):
    text = models.CharField(max_length=100)
    category = models.CharField(max_length=12)
    def __str__(self):
        return self.text

class Question(models.Model):
    text = models.CharField(max_length=250)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=12)
    quizzes = models.ManyToManyField(Quiz)
    def __str__(self):
        return self.text


class QuizContent(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.question.text
    
class Record(models.Model):
    officer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_score = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
