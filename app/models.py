#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_images = models.FileField(upload_to='user_profile_images', null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    SEX_CHOICES = (
        ('female', u'女'),
        ('male', u'男'),
        ('secret', u'保密'),
    )
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, null=True, blank=True)
    last_visit_dt = models.DateTimeField(null=True, blank=True)
    full_profile = models.BooleanField(default=False)

    def __str__(self):
        return self.belong_to

class Question(models.Model):
    questioner = models.ForeignKey(to=UserProfile, related_name='user_question')
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=6000, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    belong_to_question = models.ForeignKey(to=Question, related_name='question_answer')
    answerer = models.ForeignKey(to=UserProfile, related_name='user_answer')
    content = models.CharField(max_length=10000)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'%s的答案' % self.answerer