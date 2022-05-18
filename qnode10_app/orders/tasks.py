from celery import Celery
from django.core.mail import send_mail
from .models import Order

app=Celery()

