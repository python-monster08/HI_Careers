from django.db import models
from content_manager.models import Exam
# Create your models here.
class HIATeam(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    email = models.EmailField()
    # Add more fields as needed
    def __str__(self):
        return self.name
    
class Finance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    def __str__(self):
        return self.student