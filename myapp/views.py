from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from celery.result import AsyncResult
import logging

from .tasks import *

logger = logging.getLogger('celery')

def index(request):
    logger.info(f'Email sending to "srjthapa53@gmail.com"...')
    send_mail_task.delay()
    return HttpResponse("<h1>Sending Email</h1>")


def doc_to_pdf(request):
    if request.method == 'POST':
        received_file = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save(received_file.name, received_file)
        uploaded_file_url = fs.url(file_name)
        data = convert_doc_to_pdf.delay(received_file.name)
        return redirect('myapp:check_status', data.task_id)

    return render(request, 'myapp/doc-to-pdf.html')


def check_status(request, task_id):
    res = AsyncResult(task_id)
    print(res.ready())
    context = {'task_status': res.ready()}
    return render(request, 'myapp/progress.html', context)