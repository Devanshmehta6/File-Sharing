from django.http import FileResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import UploadedFile

# Create your views here.
def index(request):
    files = UploadedFile.objects.all()
    return render(request, 'index.html', {'files': files})

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        # fs.save(uploaded_file.name, uploaded_file)
        UploadedFile.objects.create(file=uploaded_file)
    return redirect('index')

def download_file(request, file_id):
    # uploaded_file = UploadedFile.objects.get(pk=file_id)
    # return redirect(uploaded_file.file.url)
    uploaded_file = get_object_or_404(UploadedFile, pk=file_id)
    file_path = uploaded_file.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)