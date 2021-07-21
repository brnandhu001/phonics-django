from django.shortcuts import render
from.models import word

# Create your views here.
def home(request):
    product = word.objects.all()
    return render(request,'home.html',{'product':product})
def own(request,id):
    product = word.objects.get(id=id)
    return render(request, 'own.html',{'product':product})

def search(request):
    if request.method=='POST':
        searched= request.POST['searched']
        product=word.objects.filter(regular_word__contains=searched)
        return render(request, 'search.html',{'searched':searched,' product': product})
    else:
        return render(request, 'search.html')
