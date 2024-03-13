# admin.py

from django.contrib import admin
from .models import Exam, Area, Part, Topic, Subtopic, Book, Note, Syllabus, QuestionBank, HIATeam, Student, Finance

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_category']

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'area_category']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'part_category']

@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic_category']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publication_date', 'area']

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'area']

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['title', 'area']

@admin.register(QuestionBank)
class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ['title', 'area']

@admin.register(HIATeam)
class HIATeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'contact']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam', 'enrollment_date', 'email']

@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'transaction_date', 'amount', 'description']
