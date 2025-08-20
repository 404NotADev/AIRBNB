from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from bookings.models import Booking

@shared_task
def send_booking_email(booking_id):
    try:
        booking = Booking.objects.select_related("listing", "guest", "listing__owner").get(id=booking_id)
    except Booking.DoesNotExist:
        return f"Booking {booking_id} does not exist"

    subject = f"Booking Confirmed: {booking.listing.title}"


    message_guest = f"Hello {booking.guest.username}, your booking at {booking.listing.title} is confirmed!\n" \
                    f"Check-in: {booking.check_in}, Check-out: {booking.check_out}."

  
    message_host = f"Hello {booking.listing.owner.username}, you have a new booking for {booking.listing.title}!\n" \
                   f"Guest: {booking.guest.username}, Dates: {booking.check_in} - {booking.check_out}."

    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "imanalievdanielsamarovich@gmail.com")

    
    send_mail(subject, message_guest, from_email, [booking.guest.email])
    send_mail(subject, message_host, from_email, [booking.listing.owner.email])

    return f"Emails sent for booking {booking_id}"
