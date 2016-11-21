from django import forms
from django.core.exceptions import ValidationError
from app.models import UserProfile


def words_validator(answer):
    if len(answer) < 1:
        raise ValidationError('一个字都不说不太好吧！')


def answer_validator(answer):
    INVALID_WORDS = ['傻b', '傻逼', '脑残', 'sb', '尼玛', '妈']
    if any(answer.__contains__(word) for word in INVALID_WORDS):
        raise ValidationError('艹，想骂人是不是！')


class AnswerForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea(),
                              error_messages={
                                  'required': '一个字都不说不太好吧！'
                                  },
                              validators=[words_validator, answer_validator])


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(),
                              error_messages={
                                  'required': '一个字都不说不太好吧！'
                                  },
                              validators=[words_validator, answer_validator])
