from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

from .task import *

def index(request):
    send_mail_task.delay()
    return HttpResponse("<h1>Hello world</h1>")
