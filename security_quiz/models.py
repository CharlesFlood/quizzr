# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

OFFICER_AUTH_LEVELS = (
    ('AL','Alpha Lead'),
    ('AM','Alpha Member'),
    ('BL','Bravo Lead'),
    ('BM','Bravo Member'),
    ('TL','Tango Lead',),
    ('TM','Tango Member'),
)

class Answer(models.Model):
    text = models.CharField(max_length=100)
    category = models.CharField(max_length=12)

class Question(models.Model):
    text = models.CharField(max_length=250)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=12)

### The Officer class should probably be replaced with the django user class
class Officer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    auth_level = models.CharField(max_length=2, choices=OFFICER_AUTH_LEVELS)

class Quiz(models.Model):
    name = models.CharField(max_length=20)

class QuizContents(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
class Record(models.Model):
    officer = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_given = models.ForeignKey(Answer, on_delete=models.CASCADE)
    
