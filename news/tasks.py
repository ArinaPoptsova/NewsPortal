import datetime
import json

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news.models import Category


@shared_task(serializer='json')
def notify_new_post(request_data, categories_id, *args, **kwargs):
    news = request_data
    categories = [Category.objects.get(id=id) for id in map(int, categories_id)]
    html_content = render_to_string(
        'message.html',
        {
            'news': news,
            'news_object': categories[0].post_set.all().last(),
        }
    )
    msg = EmailMultiAlternatives(
        subject=news['title'],
        body=news['text'],
        from_email='lolkovalolka@yandex.ru',
        to=[subscriber.email for cat in categories for subscriber in cat.subscribers.all()]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task()
def mailing():
    for category in Category.objects.all():
        posts = category.post_set.filter(date__gt=datetime.datetime.now(tz=None) - datetime.timedelta(days=2))
        html_content = render_to_string(
            'mailing.html',
            {
                'posts': posts
            }
        )
        msg = EmailMultiAlternatives(
            subject='Posts of your favorite category',
            body='There are no any posts yet',
            from_email='lolkovalolka@yandex.ru',
            to=[subscriber.email for subscriber in category.subscribers.all()]
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
