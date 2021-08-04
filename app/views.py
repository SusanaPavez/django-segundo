from django.shortcuts import render, HttpResponse
from time import localtime, strftime

def second(request, name):
    return HttpResponse('Hola ' + name)


def index(request):
    context = {
        "localtime": strftime("%Y-%m-%d %H:%M", localtime())
    }
    return render(request,'index.html', context)
