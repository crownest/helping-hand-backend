# Django
from django.core.mail import send_mail


def mail_task(context):
    """
    Context Format
        context = {
            subject="subject"
            message="messages"
            html_message=render_to_string('email/email.html', template_context),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        }
    """

    try:
        return send_mail(**context)
    except Exception as e:
        print(e)
        pass
