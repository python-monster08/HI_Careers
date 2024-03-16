from django.contrib import admin
from .models import HIATeam, Student, Finance
# Register your models here.
@admin.register(HIATeam)
class HIATeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'contact']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam', 'enrollment_date', 'email']

@admin.register(Finance)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'transaction_date', 'amount', 'description']
