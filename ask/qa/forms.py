from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data['text']
        return text

    def save(self):
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    # def clean_question(self):
    #     question_id = self.cleaned_data.get('question')
    #     try:
    #         question = Question.objects.get(id=question_id)
    #     except Question.DoesNotExist:
    #         question = None
    #     return question
    #
    # def clean_text(self):
    #     text = self.cleaned_data.get('text')
    #     if text.strip() == '':
    #         raise forms.ValidationError(_('Text is empty'), code='Validation_Error')
    #     return text
    #
    # def save(self):
    #     self.cleaned_data['question'] = get_object_or_404(Question, pk=slef.cleaned_data['question'])
    #     if self._user.is_anonymous():
    #         self.cleaned_data['author_id'] = 1
    #     else:
    #         self.cleaned_data['author'] = self._user
    #     answer = Answer(**self.cleaned_data)
    #     answer.save()
    #     return answer
    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer
