from django.db import models

# Create your models here.
# Exam Category
class Exam(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Area Category
class Area(models.Model):
    name = models.CharField(max_length=100)
    exam_category = models.ForeignKey(Exam, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Part Category
class Part(models.Model):
    name = models.CharField(max_length=100)
    area_category = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
# Topic Category
class Topic(models.Model):
    name = models.CharField(max_length=100)
    part_category = models.ForeignKey(Part, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
# Subtopic Category
class Subtopic(models.Model):
    name = models.CharField(max_length=100)
    topic_category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Book Management by Area
class Book(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    file = models.FileField(upload_to='BookFiles')
    def __str__(self):
        return self.title
    
# Notes Management by Area
class Note(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='NotesFiles')
    def __str__(self):
        return self.title

# Syllabus Management by Area
class Syllabus(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='SyllabusFiles')
    def __str__(self):
        return self.title

# QuestionBank Management by Area
class QuestionBank(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='QuestionBankFiles')
    def __str__(self):
        return self.title
    
