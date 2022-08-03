from django.core.mail import send_mail


def send_email(*, subject, body, to_email, from_email):
    try:
        send_mail(subject=subject, message=body, from_email=from_email, recipient_list=[to_email], fail_silently=False)
    except Exception as e:
        # @TODO log e
        pass