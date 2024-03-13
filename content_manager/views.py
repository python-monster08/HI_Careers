from django.shortcuts import render
import os
from django.http import HttpResponse
from .forms import FileUploadForm
from .utils import extract_text_from_pdf, extract_text_from_docx, extract_text_from_pptx

# Create your views here.
def files_generater_or_uploader(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name
            file_extension = os.path.splitext(file_name)[1].lower()
            
            # Save the uploaded file to a temporary location or process in-memory
            # handle_uploaded_file(uploaded_file)

            # Check file extension and call the appropriate extraction function
            if file_extension == '.pdf':
                text = extract_text_from_pdf(uploaded_file)
            elif file_extension == '.docx':
                text = extract_text_from_docx(uploaded_file)
            elif file_extension == '.pptx':
                text = extract_text_from_pptx(uploaded_file)
            else:
                return HttpResponse('Unsupported file type.', status=400)
            
            # You can now do something with the extracted text
            # For this example, we'll just return it as an HTTP response
            return HttpResponse(text, content_type="text/plain")
    else:
        form = FileUploadForm()

    # return render(request, 'upload.html', {'form': form})
    return render(request, 'content_manager/files_genrater_or_uploader.html', {'form': form})