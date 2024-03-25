from django.http import HttpResponse
from django.shortcuts import render
from .forms import DocumentUploadForm
from .utils import parse_string


def index(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['document']
            content = uploaded_file.read().decode('utf-8')
            data = parse_string(content)
            return render(request, 'index.html', {'form': form, 'data': data})
        return HttpResponse("error")
        # return render
    else:
        form = DocumentUploadForm()

    return render(request, 'index.html', {'form': form})
