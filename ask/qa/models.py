from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.ImageField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def new(self):
        pass

    def popular(self):
        pass


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
