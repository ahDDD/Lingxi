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
    TITLE_CHOICES = (
        (u'教授', u'教授'),
        (u'副教授', u'副教授'),
        (u'博士', u'博士'),
        (u'硕士', u'硕士'),
    )
    title = models.CharField(choices=TITLE_CHOICES, max_length=10, null=True, blank=True)
    sex = models.CharField(choices=SEX_CHOICES, max_length=10, null=True, blank=True)
    last_visit_dt = models.DateTimeField(null=True, blank=True)
    full_profile = models.BooleanField(default=False)


    def __str__(self):
        return str(self.belong_to)


class Question(models.Model):
    questioner = models.ForeignKey(to=UserProfile, related_name='user_question')
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=6000, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)


    def __str__(self):
    #def __unicode__(self):
        return self.title


class Answer(models.Model):
    belong_to_question = models.ForeignKey(to=Question, related_name='question_answer')
    answerer = models.ForeignKey(to=UserProfile, related_name='user_answer')
    content = models.CharField(max_length=10000)
    best_answer = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    #def __unicode__(self):
    def __str__(self):
        return u'%s的答案' % self.answerer


class Comment(models.Model):
    user = models.ForeignKey(to=User, related_name='user_comment', null=True,
                             blank=True)
    comment = models.TextField()
    belong_to_answer = models.ForeignKey(to=Answer, related_name='under_comments',
                                  null=True, blank=True)
    best_comment = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ':' + self.comment
