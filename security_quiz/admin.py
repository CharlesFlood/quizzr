# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Answer, Question, Quiz, QuizContent, Record
# Register your models here.

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(QuizContent)
admin.site.register(Record)
