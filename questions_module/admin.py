from django.contrib import admin
from .models import QuestionType, DegreeOfDifficulty, Question

# Register your models here.
admin.site.register(QuestionType)
admin.site.register(DegreeOfDifficulty)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_type', 'question', 'marks', 'negative_marks', 'created_at', 'updated_at')
    list_filter = ('question_type', 'created_at', 'updated_at')
    search_fields = ('question', 'subject_of_exam', 'sub_topic', 'assigned_to')
