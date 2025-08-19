from celery import shared_task
from django.core.mail import send_mail
from listings.models import Listing

@shared_task
def notify_host_new_listing(listing_id):
    listing = Listing.objects.get(id=listing_id)
    subject = f"Your listing '{listing.title}' is now live!"
    message = f"Congrats {listing.owner.username}, your listing '{listing.title}' has been published."
    send_mail(subject, message, 'noreply@airbnbclone.com', [listing.owner.email])
