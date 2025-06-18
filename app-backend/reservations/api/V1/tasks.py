from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_reservation_email(name, email, date, time):
    subject = "تأیید رزرو میز"
    
    message = f"""
    سلام {name} عزیز 🌸،

    رزرو شما برای تاریخ {date} ساعت {time} با موفقیت ثبت شد.
    
    با تشکر از اعتماد شما،
    رستوران ما
    """

    html_message = f"""
    <html>
        <body style="font-family:Tahoma, sans-serif; direction:rtl; text-align:right;">
            <h3>سلام {name} عزیز 🌸</h3>
            <p>رزرو شما برای تاریخ <strong>{date}</strong> ساعت <strong>{time}</strong> با موفقیت ثبت شد.</p>
            <p>با تشکر از اعتماد شما،<br>رستوران ما</p>
        </body>
    </html>
    """

    from_email = "no-reply@restaurant.com"
    recipient_list = [email]

    try:
        send_mail(
            subject=subject,
            message=message.strip(),
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
            html_message=html_message
        )
    except Exception as e:
        logger.error(f"خطا در ارسال ایمیل رزرو برای {email}: {e}")
        raise
