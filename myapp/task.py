from django.core.mail import send_mail
from celery import shared_task
from time import sleep


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