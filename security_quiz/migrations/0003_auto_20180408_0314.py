# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-08 03:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security_quiz', '0002_delete_officer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuizContents',
            new_name='QuizContent',
        ),
    ]
