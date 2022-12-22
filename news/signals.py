import datetime

from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Post
from .exceptions import RequestOver


@receiver([post_save, m2m_changed], sender=Post.category.through)
def notify_new_post(sender, instance, **kwargs):
    html_content = render_to_string(
        'message.html',
        {
            'news': instance,
        }
    )
    msg = EmailMultiAlternatives(
        subject=instance.title,
        body=f'{instance.get_absolute_url()} {instance.text}',
        from_email='lolkovalolka@yandex.ru',
        to=[subscriber.email for cat in instance.category.all() for subscriber in cat.subscribers.all()]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

@receiver(pre_save, sender=Post)
def constraint_post(sender, instance, **kwargs):
    if Post.objects.filter(date__gt=datetime.date.today()).count() > 3:
        raise RequestOver
