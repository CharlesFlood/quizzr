# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from random import sample

class AnswerManager(models.Manager):
    def get_random_answers(self, category, answer_id):
        starting_set = list(super(AnswerManager, self).get_queryset().filter(category=category).exclude(pk=answer_id))
        random_list = []
        for i in sample(range(1,len(starting_set)),4):
            random_list.append(starting_set[i])
        return random_list
    
class Answer(models.Model):
    text = models.CharField(max_length=100)
    category = models.CharField(max_length=12)
    answer = AnswerManager()
    def __str__(self):
        return self.text
        

class Question(models.Model):
    text = models.CharField(max_length=250)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=12)
    def __str__(self):
        return self.text

class QuizManager(models.Manager):
    def available_quizzes(self, officer):
        if officer.has_perm('alpha'):
            starting_set = super(QuizManager, self).get_queryset()
        if officer.has_perm('bravo'):
            starting_set = super(QuizManager, self).get_queryset().exclude(auth_level="alpha")
        if officer.has_perm('tango'):
            starting_set = super(QuizManager, self).get_queryset().filter(auth_level="tango")
        return starting_set
    def passed_quizzes(self, officer):
        
    def unpassed_quizzes(self, officer):
        pass
    
class BravoQuizManager(models.Manager):
    def available_quizzes(self):
        return super(BravoQuizManager, self).get_queryset().exclude(auth_level="alpha")
class TangoQuizManager(models.Manager):
    def available_quizzes(self):
        return super(TangoQuizManager, self).get_queryset().filter(auth_level="tango")
    
class Quiz(models.Model):
    AUTH_LEVELS = (
        ('alpha','Alpha'),
        ('bravo','Bravo'),
        ('tango','Tango'),
    )
    name = models.CharField(max_length=20)
    opening_text = models.CharField(max_length=240)
    auth_level = models.CharField(max_length=5, choices=AUTH_LEVELS)
    questions = models.ManyToManyField(Question)
    active_duration = models.IntegerField(default=365) # in days
    alpha_quizzes = models.Manager() #exclude nothing
    bravo_quizzes = BravoQuizManager() #exclude alpha
    tango_quizzes = TangoQuizManager() #exclude alpha/bravo
    quizzes = QuizManager()
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "quizzes"
        permissions = (
            ("alpha","Can take alpha level tests"),
            ("bravo","Can take bravo level tests"),
            ("tango","Can take tango level tests"),
        )
    
class Record(models.Model):
    officer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_score = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
