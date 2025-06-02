# from django.core.mail import send_mail

# def send_reservation_email(reservation):
#     send_mail(
#         subject="تأیید رزرو میز",
#         message=f"سلام {reservation.name}، رزرو شما برای {reservation.date} ساعت {reservation.time} ثبت شد.",
#         from_email="no-reply@restaurant.com",
#         recipient_list=[reservation.email],
#         fail_silently=False,
#     )
