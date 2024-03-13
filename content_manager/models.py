from django.db import models

# Create your models here.

class Exam(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)
    exam_category = models.ForeignKey(Exam, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Part(models.Model):
    name = models.CharField(max_length=100)
    area_category = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    name = models.CharField(max_length=100)
    part_category = models.ForeignKey(Part, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Subtopic(models.Model):
    name = models.CharField(max_length=100)
    topic_category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    content = models.TextField()
    def __str__(self):
        return self.title
    
class Note(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title

class Syllabus(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title

class QuestionBank(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title
    
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