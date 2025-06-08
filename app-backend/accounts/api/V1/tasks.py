from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


@shared_task
def send_email_with_celery(template: str, subject: str, context: dict, from_email: str, recipient_list: list):
    """
    Renders an email from HTML template and sends it asynchronously.

    Args:
        template (str): Path to HTML template.
        subject (str): Subject of the email.
        context (dict): Context to render in the template.
        from_email (str): Sender's email.
        recipient_list (list): List of recipient emails.
    """
    html_content = render_to_string(template, context)

    email = EmailMessage(
        subject=subject,
        body=html_content,
        from_email=from_email,
        to=recipient_list,
    )
    email.content_subtype = "html"
    email.send()

