from django.urls import path
from . import views
# Create questions_module Urls here.
urlpatterns = [
    path('', views.index, name='home'),
    # path('export_word/', views.ExportWordView.as_view(), name='export_word'),
    path('export-questions/', views.generate_questions_word_document, name='export_questions'),

]
