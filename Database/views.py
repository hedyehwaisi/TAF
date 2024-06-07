from django.shortcuts import render

# Create your views here.

def Hello_there(request):
    return HttpResponse("Hello there!")