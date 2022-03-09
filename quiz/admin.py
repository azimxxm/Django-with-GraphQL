from django.contrib import admin
from .models import *

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_rigth']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['title', 'quiz']
    list_display = ['title', 'quiz']
    inlines = [AnswerInlineModel,]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_rigth', 'question']