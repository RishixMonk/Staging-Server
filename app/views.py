from django.shortcuts import render,HttpResponse
from .redisserver import f1
from .tasks import deployFromImage
# Tell RQ what Redis connection to use
     # Create your views here.

def index(request):
    return render(request,'index.html')

def id(request):
    return HttpResponse("hii")

def test(request):
    dockerimage,internalport=f1()
    deployFromImage.delay(dockerimage,internalport)
    return HttpResponse("Done")