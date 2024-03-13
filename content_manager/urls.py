from django.urls import path
from . import views
# Create questions_module Urls here.
urlpatterns = [
    # path('', views.index, name='home'),
    path('files-generater-or-uploader/', views.files_generater_or_uploader, name='files_generater_or_uploader'),
    # path('export-questions/', views.generate_questions_document, name='export_questions'),
    # path('generate-csv/', views.generate_questions_csv_view, name='generate-csv'),
]
