from celery import shared_task
from payments.models import Payment
from bookings.models import Booking

@shared_task
def update_booking_status(payment_id):
    payment = Payment.objects.get(id=payment_id)
    booking = payment.booking
    if payment.status == 'succeeded':
        booking.status = 'confirmed'
        booking.save()
