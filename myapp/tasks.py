from django.core.mail import send_mail
from celery import shared_task
from time import sleep
from docx2pdf import convert

@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    send_mail(
        "Email using django celery",
        "Hello",
        "thapasusil53@gmail.com",
        ["srjthapa53@gmail.com"],
        fail_silently=False
    )
    return None


@shared_task
def convert_doc_to_pdf(file):
    convert('media/' + file)
    return None


@shared_task
def mail_monday_motivation_quotes():
    send_mail(
        "Stay motivated",
        "Do not pray for an easy life, pray for the stength to endure difficult one.",
        "thapasusil53@gmail.com",
        ["srjthapa53@gmail.com"],
        fail_silently=False
    )
    return None