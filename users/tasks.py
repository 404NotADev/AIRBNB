from celery import shared_task
from django.core.mail import send_mail
from users.models import User

@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    subject = "Welcome to Airbnb Clone!"
    message = f"Hello {user.username}, welcome to Airbnb Clone!"
    send_mail(subject, message, 'noreply@airbnbclone.com', [user.email])
