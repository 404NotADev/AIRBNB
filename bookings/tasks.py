from celery import shared_task
from django.core.mail import send_mail
from bookings.models import Booking

@shared_task
def send_booking_email(booking_id):
    booking = Booking.objects.get(id=booking_id)
    subject = f"Booking Confirmed: {booking.listing.title}"
    message_guest = f"Hello {booking.guest.username}, your booking is confirmed!"
    message_host = f"Hello {booking.listing.owner.username}, you have a new booking!"
    
    send_mail(subject, message_guest, 'noreply@airbnbclone.com', [booking.guest.email])
    send_mail(subject, message_host, 'noreply@airbnbclone.com', [booking.listing.owner.email])
