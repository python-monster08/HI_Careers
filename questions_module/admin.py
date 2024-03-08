from django.contrib import admin
from .models import QuestionType, DegreeOfDifficulty, Question
from django.utils.html import strip_tags

# Register your models here.
@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
@admin.register(DegreeOfDifficulty)
class DegreeOfDifficultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'difficulty_title')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_type', 'display_question', 'marks', 'negative_marks', 'created_at', 'updated_at')
    list_filter = ('question_type', 'created_at', 'updated_at')
    search_fields = ('question', 'subject_of_exam', 'sub_topic', 'assigned_to')

    def display_question(self, obj):
        return strip_tags(obj.question)
    
    display_question.short_description = 'Question'

