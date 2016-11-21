from django.contrib import admin
from app.models import UserProfile, Question, Answer, Comment
# Register your models here.
admin.site.register([UserProfile, Question, Answer, Comment])
# admin.site.register(Question)
# admin.site.register(Answer)
