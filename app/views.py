from django.shortcuts import render,HttpResponseRedirect
from .tasks import deployFromImage
from .models import Info
from .forms import Infoform
from .getport import find_free_port
# Tell RQ what Redis connection to use
     # Create your views here.

def index(request):
    return render(request,'index1.html')

def id(request):
    # info=Info.objects.all()

    # for i in info:
    #     dockerimage = i.imagename
    #     internalport = i.portno
    #     deployFromImage.delay(dockerimage,internalport)
    if request.method == 'POST':
        dockerimage=request.POST['imagename']
        internalport=request.POST['portno']
        form = Infoform(request.POST)
        form.save()
        externalPort = find_free_port()
        deployFromImage.delay(dockerimage,internalPort= internalport, externalPort = externalPort)
    info = Info.objects.all()
    return render(request,'index2.html',{'info':info})

def test(request):
    # dockerimage,internalport=f1()
    # deployFromImage.delay(dockerimage,internalport)
    # if request.method == "POST":
    #     form=Infoform(request.POST)
    #     form.save()
    #     return HttpResponseRedirect('/id')
    form=Infoform
    return render(request,'index.html',{'form':form})