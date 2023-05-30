from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Review


@receiver(post_save, sender=Review)
def notify_abt_reply(sender, instance, created, **kwargs):
    template = None
    first_name = None
    commentator = None
    subject = None
    email = None

    text_reply = instance.text
    link_post = f'{settings.SITE_URL}/{instance.movie.url}'

    if created:
        print('Hello, I am a created comment!!!')
        user = instance.commentator
        first_name = user.first_name or user.username
        template = 'comment_created.html'

        commentator = instance.commentator
        subject = f'{settings.SITE_URL}/{instance.movie.url}! You have new reply on ur comment'
        email = user.email or ""


    else:
        # Handle other cases if necessary
        return

    html_content = render_to_string(
        f'{template}',
        {
            'user': user,
            'commentator': commentator,
            'name': first_name,
            'text_reply': text_reply,
            'link': link_post,
        }
    )

    message = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )
    print(email)
    message.attach_alternative(html_content, 'text/html')
    message.send()
