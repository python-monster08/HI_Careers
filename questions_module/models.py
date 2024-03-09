from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
import json

class QuestionType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name
    
class DegreeOfDifficulty(models.Model):
    difficulty_title = models.CharField(max_length=255)

    def __str__(self):
        return self.difficulty_title
    
class Question(models.Model):
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question = models.TextField()  # Changed to TextField for longer questions

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255, null=True, blank=True)
    option_c = models.CharField(max_length=255, null=True, blank=True)
    option_d = models.CharField(max_length=255, null=True, blank=True)

    correct_answer_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    correct_answer_description = models.TextField()  # Changed to TextField for longer descriptions

    marks = models.IntegerField()
    negative_marks = models.IntegerField(null=True, blank=True)

    name_of_exam = models.CharField(max_length=255, null=True, blank=True)
    year_of_exam = models.CharField(max_length=4, null=True, blank=True)
    subject_of_exam = models.CharField(max_length=255, null=True, blank=True)
    question_numbering_exam_paper = models.IntegerField(null=True, blank=True)

    sub_topic = models.CharField(max_length=255, null=True, blank=True)
    repeat_in_exam = models.CharField(max_length=255, null=True, blank=True)
    other = models.CharField(max_length=255, null=True, blank=True)
    degree_of_difficulty = models.ForeignKey(DegreeOfDifficulty, on_delete=models.CASCADE)
    applicability = models.CharField(max_length=255, null=True, blank=True)
    assigned_to = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Set the created_at timestamp only on the initial save
        if not self.id:
            self.created_at = timezone.now()

        # Always update the updated_at timestamp on each save
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.question_type)


