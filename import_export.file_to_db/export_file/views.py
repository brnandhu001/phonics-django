from django.shortcuts import render
from .models import word
from .resources import WordResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

# Create your views here.
def simple_upload(request):#no need everything ..upload a file in admin side..its for user side
     if request.method == 'POST':
          word_resource = WordResource()
          dataset = Dataset()
          new_word = request.FILES['myfile']

          if not new_word.name.endswith('xlsx'):
              messages.info(request,'worng format')
              return render(request,'upload.html')
          imported_data=dataset.load(new_word.read(),format='xlsx')
          for data in imported_data:
             value= word(data)
             value.save()
     return render(request,'upload.html')
def export(request):
    word_resource = WordResource()
    dataset = word_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="word.xls"'
    return response

