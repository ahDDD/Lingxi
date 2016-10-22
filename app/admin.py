from django.contrib import admin
from app.models import UserProfile, Question, Answer
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)