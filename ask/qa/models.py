# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class QuestionManager(models.Model):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    objects = QuestionManager()

    class Meta:
        ordering = ['-id']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
