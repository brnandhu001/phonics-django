from django.shortcuts import render,HttpResponse
from .models import words
from django.contrib import messages




# Create your views here.
def home(request):
    letters = words.objects.all()

    return render(request, 'home.html', {'letters': letters})


def search(request):
    if request.method=='POST':
        searched= request.POST['searched']
        letters=words.objects.filter(regular_word__contains=searched)
        return render(request, 'search.html',{'searched':searched,'letters':letters})
    else:
        return render(request, 'search.html')

def own(request,id):
    letters = words.objects.get(id=id)
    return render(request,'own.html',{'letters':letters})



