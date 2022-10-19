from django.shortcuts import render,HttpResponse
from .tasks import deployFromImage
     # Create your views here.

def index(request):
    return render(request,'index.html')

def id(request):
    return HttpResponse("hii")

def test(request):
    deployFromImage.delay()
    return HttpResponse("Done")