from celery.app import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from account.utils.tokens import account_activation_token

# http://accounts/confirmation/Nw/5rq-04ad7b7ea05b4b133bd0/
# http://accounts/confirmation/OA/5rq-e2a4ad42e3e7b40a09e4/
# http://localhost:8000/accounts/confirmation/MTA/5rq-0706b66e9541aedfad99/

@shared_task
def send_confirmation_mail(user):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    redirect_url = f"http://localhost:8000{reverse_lazy('account:confirmation', kwargs={'uidb64': uid,'token': token})}"
    body = render_to_string('email/confirmation_email.html', context={
        'user': user,
        'redirect_url': redirect_url,
    })
    msg = EmailMessage(subject='Email Verification', body=body,
                       from_email=settings.EMAIL_HOST_USER, to=[user.email],)
    msg.content_subtype = 'html'
    msg.send()