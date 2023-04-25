from celery import shared_task
from .models import Post, Subscription
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from .signals import product_created
from django.template.loader import render_to_string
from django.conf import settings
import datetime


@shared_task
def push_subscribers_monday():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_create__gte=last_week)
    categories = set(posts.values_list('category__id', flat=True))
    subscribers = set(Subscription.objects.filter(category__in=categories).values_list('user__email', flat=True))
    content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject="Новые статьи в ваших категориях",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(content, 'text/html')
    msg.send()


@shared_task
def push_subscribers(instance, created, **kwargs):
    if not created:
        return
    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новый пост в категории {instance.category}'

    text_content = (
        f'Тема: {instance.title}\n'
        f'Текст: {instance.text[0:21]}\n\n'
        f'Ссылка на пост: http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Тема: {instance.title}<br>'
        f'Текст: {instance.text[0:21]}<br><br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
