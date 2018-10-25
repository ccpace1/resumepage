from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Testing")
    return render(request, "resume_app/welcome.html")
