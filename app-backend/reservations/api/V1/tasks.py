from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reservation_email(name, email, date, time):
    subject = "تأیید رزرو میز"
    message = f"  سلام {name} عزیز 🌸، رزرو شما برای تاریخ {date} ساعت {time} ثبت شد."
    from_email = "no-reply@restaurant.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
