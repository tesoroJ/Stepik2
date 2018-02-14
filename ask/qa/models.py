from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        #return self.order_by('-rating')
        return self.order_by('-id')


class Question(models.Model):
    # objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/question/%d/' % self.pk

    objects = QuestionManager()

    class Meta:
        ordering = ['-id']


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return '/question/%d/' % self.question.id

    def __str__(self):
        return self.text

